"""
    GeoReport v2 Server
    -------------------

    Container for service types and definitions.

    :copyright: (c) Code for America 2012
    :author: Jesse Bounds (@boundsj)
    :license: Apache License v2.0, see LICENSE for more details.
"""

api_keys = ['xyz', '12345', '3k76HOWQ']

service_discovery = {
  "changeset":"2012-01-14 12:00",
  "contact":"Currently, no support is available",
  "key_service":"Coming soon!",
  "endpoints":[
    {
      "specification":"http://wiki.open311.org/GeoReport_v2",
      "url":"http://open311.mycity.gov/v2",
      "changeset":"2010-11-23 09:01",
      "type":"production",
      "formats":[
        "text/xml"
      ]
    },
    {
      "specification":"http://wiki.open311.org/GeoReport_v2",
      "url":"http://open311.mycity.gov/test/v2",
      "changeset":"2010-10-02 09:01",
      "type":"test",
      "formats":[
        "text/xml",
        "application/json"
      ]
    },
    {
      "specification":"http://wiki.open311.org/GeoReport_v3",
      "url":"http://open311.mycity.gov/v3",
      "changeset":"2011-02-03 14:18",
      "type":"test",
      "formats":[
        "text/xml",
        "application/json"
      ]
    }
  ]
}

service_types = [
  {
    "service_code":"CFA1",
    "service_name":"Beverage Issues",
    "description":"Coffee pots not full and empty beer bottles are not tolerated. Violators will be cited.",
    "metadata":False,
    "type":"realtime",
    "keywords":"beverage, beer, coffee, drinks",
    "group":"libations"
  },
  {
    "service_code":"CFA2",
    "metadata":False,
    "type":"realtime",
    "keywords":"dishes, ",
    "group":"dishes",
    "service_name":"Dish left out",
    "description":"Someone was a cotton-headed ninny-muggins and left a dish out and unwashed."
  }
]

service_definitions = {
    'CFA': {
  "service_code":"CFA1",
  "attributes":[
    {
      "variable":True,
      "code":"WHISHETN",
      "datatype":"singlevaluelist",
      "required":True,
      "datatype_description":None,
      "order":1,
      "description":"What is the twitter tag?",
      "values":[
        {
          "key":1,
          "name":"#cfanocoffee"
        },
        {
          "key":2,
          "name":"#cfanobeer"
        }
      ]
    }
  ]
}

}

# Dummy service requests
srs = [
  {
    "service_request_id":638344,
    "status":"closed",
    "status_notes":"Duplicate request.",
    "service_name":"Sidewalk and Curb Issues",
    "service_code":006,
    "description":None,
    "agency_responsible":None,
    "service_notice":None,
    "requested_datetime":"2010-04-14T06:37:38-08:00",
    "updated_datetime":"2010-04-14T06:37:38-08:00",
    "expected_datetime":"2010-04-15T06:37:38-08:00",
    "address":"8TH AVE and JUDAH ST",
    "address_id":545483,
    "zipcode":94122,
    "lat":37.762221815,
    "long":-122.4651145,
    "media_url":"http://city.gov.s3.amazonaws.com/requests/media/638344.jpg"
  },
  {
    "service_request_id":638349,
    "status":"open",
    "status_notes":None,
    "service_name":"Sidewalk and Curb Issues",
    "service_code":006,
    "description":None,
    "agency_responsible":None,
    "service_notice":None,
    "requested_datetime":"2010-04-19T06:37:38-08:00",
    "updated_datetime":"2010-04-19T06:37:38-08:00",
    "expected_datetime":"2010-04-19T06:37:38-08:00",
    "address":"8TH AVE and JUDAH ST",
    "address_id":545483,
    "zipcode":94122,
    "lat":37.762221815,
    "long":-122.4651145,
    "media_url":"http://city.gov.s3.amazonaws.com/requests/media/638349.jpg"
  }
]
