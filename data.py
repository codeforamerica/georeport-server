"""
    GeoReport v2 Server
    -------------------

    Container for service types and definitions.

    :copyright: (c) Miami-Dade County 2011
    :author: Julian Bonilla (@julianbonilla)
    :license: Apache License v2.0, see LICENSE for more details.
"""


api_keys = ['xyz', '12345', '3k76HOWQ']

service_discovery = {
  "changeset":"2011-02-03 14:18",
  "contact":"You can email or call for assistance api@mycity.org +1 (555) 555-5555",
  "key_service":"You can request a key here: http://api.mycity.gov/api_key/request",
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
    "service_code":001,
    "service_name":"Cans left out 24x7",
    "description":"Garbage or recycling cans that have been left out for more than 24 hours after collection. Violators will be cited.",
    "metadata":False,
    "type":"realtime",
    "keywords":"lorem, ipsum, dolor",
    "group":"sanitation"
  },
  {
    "service_code":002,
    "metadata":False,
    "type":"realtime",
    "keywords":"lorem, ipsum, dolor",
    "group":"street",
    "service_name":"Construction plate shifted",
    "description":"Metal construction plate covering the street or sidewalk has been moved."
  },
  {
    "service_code":003,
    "metadata":False,
    "type":"realtime",
    "keywords":"lorem, ipsum, dolor",
    "group":"street",
    "service_name":"Curb or curb ramp defect",
    "description":"Sidewalk curb or ramp has problems such as cracking, missing pieces, holes, and/or chipped curb."
  },
  {
    "service_code":"DMV66",
    "metadata":True,
    "type":"realtime",
    "keywords":"lorem, ipsum, dolor",
    "group":"street",
    "service_name":"Illegal Parking",
    "description":"Vehicle parked in no parking zone."
  }

]

service_definitions = {
    'DMV66': {
  "service_code":"DMV66",
  "attributes":[
    {
      "variable":True,
      "code":"WHISHETN",
      "datatype":"singlevaluelist",
      "required":True,
      "datatype_description":None,
      "order":1,
      "description":"What is the ticket/tag/DL number?",
      "values":[
        {
          "key":123,
          "name":"Ford"
        },
        {
          "key":124,
          "name":"Chrysler"
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
