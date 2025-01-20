# =====================================================================================================================
# Test configuration for Flask-assets
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


from pathlib import Path

import pytest
from flask import Flask
from flask_assets import flask_assets_blueprint


@pytest.fixture
def flask_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(flask_assets_blueprint)
    flask_app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    return flask_app

    # clean up / reset resources here


@pytest.fixture
def test_client(flask_app):
    return flask_app.test_client()


@pytest.fixture
def asset_path():
    return Path(flask_assets_blueprint.root_path)


# @pytest.fixture()
# def runner(app):
#    return app.test_cli_runner()
