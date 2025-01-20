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
