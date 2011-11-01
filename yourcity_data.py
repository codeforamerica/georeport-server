"""
    GeoReport v2 Server
    -------------------

    Empty container for service types and definitions.
    Populate with city specific data and rename file data.py

    :copyright: (c) Miami-Dade County 2011
    :author: Julian Bonilla (@julianbonilla)
    :license: Apache License v2.0, see LICENSE for more details.
"""


api_keys = ['']

service_discovery = {
  "changeset":"",
  "contact":"",
  "key_service":"",
  "endpoints":[
    {
      "specification":"http://wiki.open311.org/GeoReport_v2",
      "url":"",
      "changeset":"",
      "type":"production",
      "formats":[
        "text/xml",
        "application/json"
      ]
    },
  ]
}

service_types = [
  {
    "service_code":"",
    "service_name":"",
    "description":"",
    "metadata":False,
    "type":"realtime",
    "keywords":"",
    "group":""
  },
]

service_definitions = {
    'service_code': {
  "service_code":"",
  "attributes":[
    {
      "variable":True,
      "code":"",
      "datatype":"",
      "required":True,
      "datatype_description":None,
      "order":1,
      "description":"",
      "values":[
        {
          "key":123,
          "name":""
        },
        {
          "key":124,
          "name":""
        }
      ]
    }
  ]
}
}

# Dummy service requests
srs = [
  {
    "service_request_id":1,
    "status":"",
    "status_notes":"",
    "service_name":"",
    "service_code":1,
    "description":None,
    "agency_responsible":None,
    "service_notice":None,
    "requested_datetime":"",
    "updated_datetime":"",
    "expected_datetime":"",
    "address":"",
    "address_id":"",
    "zipcode":"",
    "lat":"",
    "long":"",
    "media_url":""
  },
]
