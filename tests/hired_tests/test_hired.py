import json


class TestHiredFunctions:

    def test_01_alive(self, client):
        rv = client.get("/")
        assert int(rv.status_code) == 200

    def test_02_template(self, client):
        rv = client.get("/")
        assert "<!-- using template! -->" in rv.data

    def test_03_api_post(self, client):
        for x in range(50):
            rv = client.post("/api/v1/snort/rules/", data=json.dumps(
                {"rule": "alert tcp any any -> any 80 (msg:\"WEB-MISC phf attempt\"; flags:A+; content:\"/cgi-bin/phf\"; priority:10;)"}))
            assert json.loads(rv.data)
            assert int(rv.status_code) == 201
            assert '"url":' in rv.data

        rv = client.post("/api/v1/snort/rules/", data="This is not json whaaaat")
        assert json.loads(rv.data)
        assert int(rv.status_code) == 400

        rv = client.post("/api/v1/snort/rules/", data=json.dumps(
            {"fail": "alert tcp any any -> any 80 (msg:\"WEB-MISC phf attempt\"; flags:A+; content:\"/cgi-bin/phf\"; priority:10;)"}))
        assert json.loads(rv.data)
        assert int(rv.status_code) == 400

    def test_04_api_get(self, client):
        rv = client.get("/api/v1/snort/rules/1")
        assert json.loads(rv.data)
        assert "alert" in rv.data

        rv = client.get("/api/v1/snort/rules/9000")
        assert int(rv.status_code) == 404

        rv = client.get("/api/v1/snort/rules/")
        assert json.loads(rv.data)
        assert "alert" in rv.data
