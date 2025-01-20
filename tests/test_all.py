# =====================================================================================================================
# Test for Flask-assets
# =====================================================================================================================
# Copyright (C) 2025 Gustavo Arzola <gustavo@xcode.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


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
