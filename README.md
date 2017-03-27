OpenCTF // Filestore
====================

This is a static file server, responsible for serving not only web assets, but also user avatars and challenge-related files (autogen included). It runs a Flask app on port 8000, listening internally from the main web application for uploads, and then serves the files using an Nginx server that is proxied from the main server.


Contact
-------

Authors: Michael Zhang, David Hou, James Wang

Copyright: EasyCTF Team

License: TBD

Email: team@easyctf.com