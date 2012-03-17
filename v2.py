"""
    GeoReport v2 Server
    -------------------

    Open311 GeoReport v2 Server implementation written in Flask.

    :copyright: (c) Miami-Dade County 2011
    :author: Julian Bonilla (@julianbonilla)
    :license: Apache License v2.0, see LICENSE for more details.
"""
from data import service_types, service_definitions, service_discovery, srs
from flask import Flask, render_template, request, abort, json, jsonify, make_response
import random, datetime
import pymongo
import iso8601

# Configuration
DEBUG = True
ORGANIZATION = 'Chicago'
JURISDICTION = 'cityofchicago.org'

DB_HOST = 'localhost'
DB_PORT = 27017
DB_NAME = '311Data'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('GEOREPORT_SETTINGS', silent=True)

# TODO: leaving the connection sitting here globally is probably not so great
mongo_connection = pymongo.Connection(DB_HOST, DB_PORT)
db = mongo_connection[DB_NAME]


@app.route('/')
def index():
    return render_template('index.html', org=app.config['ORGANIZATION'], 
                           jurisdiction=app.config['JURISDICTION'])


@app.route('/discovery.<format>')
def discovery(format):
    """Service discovery mechanism required for Open311 APIs."""
    if format == 'json':
        return jsonify(service_discovery)
    elif format == 'xml':
        response = make_response(render_template('discovery.xml', discovery=service_discovery))
        response.headers['Content-Type'] = 'text/xml; charset=utf-8'
        return response
    else:
        abort(404)


@app.route('/services.<format>')
def service_list(format):
    """Provide a list of acceptable 311 service request types and their 
    associated service codes. These request types can be unique to the
    city/jurisdiction.
    """
    def clean_id(document):
      del document['_id']
      return document
      
    services = map(clean_id, db.Services.find())
    if format == 'json':
        response = make_response(json.dumps(services))
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
    elif format == 'xml':
        response = make_response(render_template('services.xml', services=services))
        response.headers['Content-Type'] = 'text/xml; charset=utf-8'
        return response
    else:
        abort(404)


@app.route('/services/<service_code>.<format>')
def service_definition(service_code, format):
    """Define attributes associated with a service code.
    These attributes can be unique to the city/jurisdiction.
    """
    # TODO: return a dummy for any given service, since we don't have the relevant info for this
    if service_code not in service_definitions:
        abort(404)

    if format == 'json':
        return jsonify(service_definitions[service_code])
    elif format == 'xml':
        response = make_response(render_template('definition.xml',
                                                 definition=service_definitions[service_code]))
        response.headers['Content-Type'] = 'text/xml; charset=utf-8'
        return response
    else:
        abort(404)


@app.route('/requests.<format>', methods=['GET', 'POST'])
def service_requests(format):
    """"Create service requests.
    Query the current status of multiple requests.
    """
    if format not in ('json', 'xml'):
        abort(404)

    if request.method == 'POST':
        # Create service request
        sr = save(request.form)
        if format == 'json':
            return jsonify(sr)
        elif format == 'xml':
            repsonse = make_response(render_template('success.xml', sr=sr))
            response.headers['Content-Type'] = 'text/xml; charset=utf-8'
            return response
    else:
        # Return a list of SRs that match the query
        srs = search(request.args)
        if format == 'json':
            response = make_response(json.dumps(srs))
            response.headers['Content-Type'] = 'application/json; charset=utf-8'
            return response
        elif format == 'xml':
            response = make_response(render_template('service-requests.xml', service_requests=srs))
            response.headers['Content-Type'] = 'text/xml; charset=utf-8'
            return response


@app.route('/requests/<service_request_id>.<format>')
def service_request(service_request_id, format):
    """Query the current status of an individual request."""
    # TODO: handle bad request ids
    result = get_single_service_request(service_request_id)
    if format == 'json':
        return jsonify(result)
    elif format == 'xml':
        response = make_response(render_template('service-requests.xml', service_requests=[result]))
        response.headers['Content-Type'] = 'text/xml; charset=utf-8'
        return response
    else:
        abort(404)


@app.route('/tokens/<token>.<format>')
def token(token, format):
    """Get a service request id from a temporary token. This is unnecessary
    if the response from creating a service request does not contain a token.
    """
    abort(404)


def get_single_service_request(id):
  # TODO: handle bad IDs
  # TODO: handle multiple listings in DB :\
  result = db.ServiceRequests.find_one({ 'service_request_number': id })
  return format_request_for_georeport(sr)


def format_request_for_georeport(request):
  """Format an SR from the database to match Open311"""
  result = {
    'service_request_id': request['service_request_number'],
    'status': request['status'] == 'completed' and 'closed' or request['status'],
    'service_name': request['service_request_type'],
    'service_code': 'UHOH', # TODO: fix this
    'description': '', # we don't have this
    'requested_datetime': request['creation_date'],
    'updated_datetime': request['updated_on'],
    'address': request['address'],
    'address_id': '', # don't have this
    'zipcode': request['zip'],
    'lat': request['latitude'],
    'long': request['longitude'],
  }
  return result


def search(args):
    """Query service requests"""
    print json.dumps(args)
    query = {}
    if 'service_request_id' in args:
      query = { 'service_request_number': { '$in': map(lambda item: item.strip(), args['service_request_id'].split(',')) } }
      
    else:
      if 'status' in args:
        statuses = map(lambda item: item.lower().strip(), args['status'].split(','))
        statuses = map(lambda item: item == 'closed' and 'completed' or item, statuses)
        query['status'] = { '$in': statuses }
      
      if 'service_code' in args:
        query['service_request_code'] = { '$in': map(lambda item: item.strip(), args['service_code'].split(',')) }
      
      if 'start_date' in args:
        query['created'] = { '$gte': iso8601.parse_date(args['start_date']) }
      else:
        query['created'] = { '$gte': datetime.datetime.now() - datetime.timedelta(90) }
      
      if 'end_date' in args:
        end = iso8601.parse_date(args['end_date'])
        if 'created' in query:
          query['created']['$lte'] = end
        else:
          query['created'] = { '$lte': end }
    
    results = map(format_request_for_georeport, db.ServiceRequests.find(query))
    return results


def save(service_request):
    """Save service request"""
    # Implementation specific.  Just return a random SR id for now
    return {'service_request_id':random.randint(1,10000)}


if __name__ == '__main__':
    app.run()
