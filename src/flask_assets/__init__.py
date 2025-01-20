# =====================================================================================================================
# Flask Blueprint to host web framework assets
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

from flask import Blueprint, send_from_directory


flask_assets_blueprint = Blueprint("flask-assets", __name__, static_folder="assets")


@flask_assets_blueprint.route("/assets/htmx/<path:asset>", endpoint="htmx")
def send_htmx(asset):
    htmx_dir = Path(flask_assets_blueprint.root_path) / "assets" / "htmx"
    return send_from_directory(htmx_dir, asset)


@flask_assets_blueprint.route("/assets/tom-select/<path:asset>", endpoint="tom-select")
def send_tom_select(asset):
    htmx_dir = Path(flask_assets_blueprint.root_path) / "assets" / "tom-select"
    return send_from_directory(htmx_dir, asset)


@flask_assets_blueprint.route("/assets/bootstrap/<path:asset>", endpoint="bootstrap")
def send_bootstrap(asset):
    htmx_dir = Path(flask_assets_blueprint.root_path) / "assets" / "bootstrap"
    return send_from_directory(htmx_dir, asset)


@flask_assets_blueprint.route("/assets/fontawesome/<path:asset>", endpoint="fontawesome")
def send_fontawesome(asset):
    htmx_dir = Path(flask_assets_blueprint.root_path) / "assets" / "fontawesome"
    return send_from_directory(htmx_dir, asset)
