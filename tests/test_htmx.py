class TestRoot:
    def test_htmx(self, test_client, asset_path):
        path = "/assets/htmx/htmx.min.js"
        resp = test_client.get(path)
        assert resp.status == "200 OK"
        filedata = (asset_path / path[1:]).read_bytes()
        assert resp.data == filedata

    def test_fontawesome(self, test_client, asset_path):
        path = "/assets/fontawesome/css/all.min.css"
        resp = test_client.get(path)
        assert resp.status == "200 OK"
        filedata = (asset_path / path[1:]).read_bytes()
        assert resp.data == filedata

    def test_bootstrap(self, test_client, asset_path):
        path = "/assets/bootstrap/css/bootstrap.min.css"
        resp = test_client.get(path)
        assert resp.status == "200 OK"
        filedata = (asset_path / path[1:]).read_bytes()
        assert resp.data == filedata

        path = "/assets/bootstrap/js/bootstrap.min.js"
        resp = test_client.get(path)
        assert resp.status == "200 OK"
        filedata = (asset_path / path[1:]).read_bytes()
        assert resp.data == filedata

    def test_tomselect(self, test_client, asset_path):
        path = "/assets/tom-select/tom-select.bootstrap5.css"
        resp = test_client.get(path)
        assert resp.status == "200 OK"
        filedata = (asset_path / path[1:]).read_bytes()
        assert resp.data == filedata

        path = "/assets/tom-select/tom-select.complete.js"
        resp = test_client.get(path)
        assert resp.status == "200 OK"
        filedata = (asset_path / path[1:]).read_bytes()
        assert resp.data == filedata
