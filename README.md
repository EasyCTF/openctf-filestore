OpenCTF // Filestore
====================

This is a static file server, responsible for serving not only web assets, but also user avatars and challenge-related files (autogen included). It runs a Flask app on port 8000, listening internally from the main web application for uploads, and then serves the files using an Nginx server that is proxied from the main server.

To run Filestore, just run `app.py` with Python 3. It will start the Filestore server on port 7910. If you are debugging OpenCTF locally without Nginx, you can also use `/static/<path>` to retrieve saved files.

Options
-------

If you want, you can modify Filestore's behavior by setting the following environment variables:

* **FILESTORE_PORT** (defaults to 7910). Provide an integer port that the Flask server will listen on. The application will fail if your user does not have permission to use the port specified or if the port is in use.
* **UPLOAD_FOLDER** (defaults to `/usr/share/nginx/html`). Provide the path to a writeable folder that the server will save to. Ideally, the Nginx should be able to fetch directly from this directory.


Contact
-------

Authors: Michael Zhang, David Hou, James Wang

Copyright: EasyCTF Team

License: TBD

Email: team@easyctf.com