GeoReport v2 Server
===================


NOTE: This code is has been forked to CfA, this file will be updated soonish.
soon?

A simple Open311 GeoReport v2 server implementation.  Can be extended to integrate with custom 311 workflows.

http://miamidade.github.com/georeport-server/

Usage
-----
```
$ git clone http://github.com/miamidade/georeport-server.git
$ cd georeport-server
$ virtualenv env
$ . env/bin/activate
$ easy_install Flask

Run the server on localhost:5000:
$ python v2.py
```


Configuration
-------------

Set the debug mode, organization, and jurisdiction_id in [v2.py](https://github.com/miamidade/georeport-server/blob/master/v2.py).

```python
# Configuration
DEBUG = True
ORGANIZATION = 'Miami-Dade County'
JURISDICTION = 'miamidade.gov'
```

Set custom service request types, definitions, and attributes in [data.py](https://github.com/miamidade/georeport-server/blob/master/data.py).


Bug tracker
-----------

Have a bug? Please create an issue here on GitHub.

https://github.com/miamidade/georeport-server/issues


License
-------

Copyright 2011 Miami-Dade County

Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
