from cStringIO import StringIO
import os


class TestGeneral(object):

    def test_sanity(self, client):
        assert client.get("/").status_code == 200

    def test_save_prefix(self, client):
        prefix = "hello"
        file = StringIO("the quick brown fox jumps over the lazy dog")
        url = client.post(
            "/save", data=dict(file=(file, "hello.txt"), prefix=prefix)).data
        assert url[:len(prefix)] == prefix

    def test_save_suffix(self, client):
        suffix = "hello.txt"
        file = StringIO("the quick brown fox jumps over the lazy dog")
        url = client.post(
            "/save", data=dict(file=(file, "hello.txt"), suffix=suffix)).data
        assert url[-len(suffix):] == suffix

    def test_retrieved(self, app, client):
        data = "the quick brown fox jumps over the lazy dog"
        file = StringIO(data)
        url = client.post("/save", data=dict(file=(file, "hello.txt"))).data
        with open(os.path.join(app.config["UPLOAD_FOLDER"], url), "r") as f:
            assert f.read() == data
