# =====================================================================================================================
# Flask Blueprint to host web framework assets
# =====================================================================================================================

from pathlib import Path

from flask import Blueprint, send_from_directory


flask_assets_blueprint = Blueprint("flask-assets", __name__, static_folder="assets")


@flask_assets_blueprint.route("/assets/htmx/<path:assetpath>", endpoint="htmx")
def send_htmx(assetpath):
    htmx_dir = Path(flask_assets_blueprint.root_path) / "assets" / "htmx"
    return send_from_directory(htmx_dir, assetpath)


@flask_assets_blueprint.route(
    "/assets/tom-select/<path:assetpath>", endpoint="tom-select"
)
def send_tom_select(assetpath):
    htmx_dir = Path(flask_assets_blueprint.root_path) / "assets" / "tom-select"
    return send_from_directory(htmx_dir, assetpath)


@flask_assets_blueprint.route(
    "/assets/bootstrap/<path:assetpath>", endpoint="bootstrap"
)
def send_bootstrap(assetpath):
    htmx_dir = Path(flask_assets_blueprint.root_path) / "assets" / "bootstrap"
    return send_from_directory(htmx_dir, assetpath)


@flask_assets_blueprint.route(
    "/assets/fontawesome/<path:assetpath>", endpoint="fontawesome"
)
def send_fontawesome(assetpath):
    htmx_dir = Path(flask_assets_blueprint.root_path) / "assets" / "fontawesome"
    return send_from_directory(htmx_dir, assetpath)
