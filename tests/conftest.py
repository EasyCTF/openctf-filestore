import os

import pytest
from app import app as filestore_app


@pytest.fixture(scope="session")
def app(request):
    filestore_app.config["TESTING"] = True
    filestore_app.config["UPLOAD_FOLDER"] = "./.data"

    if not os.path.exists(filestore_app.config["UPLOAD_FOLDER"]):
        os.makedirs(filestore_app.config["UPLOAD_FOLDER"])

    ctx = filestore_app.test_request_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)


@pytest.fixture(scope="session")
def client(app):
    return filestore_app.test_client()
