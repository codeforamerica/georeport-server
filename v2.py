"""
    GeoReport v2 Server
    -------------------

    Open311 GeoReport v2 Server implementation written in Flask.

    :copyright: (c) Miami-Dade County 2011
    :author: Julian Bonilla (@julianbonilla)
    :license: Apache License v2.0, see LICENSE for more details.
"""
import os
from data import service_types, service_definitions, service_discovery, srs
from flask import Flask, render_template, request, abort, json, jsonify, make_response
import random

# Configuration
DEBUG = True
ORGANIZATION = 'Code for America'
JURISDICTION = 'codeforamerica.org'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('GEOREPORT_SETTINGS', silent=True)


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
    if format == 'json':
        response = make_response(json.dumps(service_types))
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
    elif format == 'xml':
        response = make_response(render_template('services.xml', services=service_types))
        response.headers['Content-Type'] = 'text/xml; charset=utf-8'
        return response
    else:
        abort(404)


@app.route('/services/<service_code>.<format>')
def service_definition(service_code, format):
    """Define attributes associated with a service code.
    These attributes can be unique to the city/jurisdiction.
    """
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
        sr = search(request.form)
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
    result = search(request.form)
    if format == 'json':
        return jsonify(srs[0])
    elif format == 'xml':
        response = make_response(render_template('service-requests.xml', service_requests=[srs[0]]))
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


def search(service_request):
    """Query service requests"""
    pass # Implementation specific


def save(service_request):
    """Save service request"""
    # Implementation specific.  Just return a random SR id for now
    return {'service_request_id':random.randint(1,10000)}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
