from flask import Flask, url_for
from flask_assets import flask_assets_blueprint

app = Flask(__name__)
app.register_blueprint(flask_assets_blueprint)


@app.route("/")
def hello_world():
    htmx = url_for("flask-assets.htmx", assetpath="htmx.min.js")
    fontawesome_css1 = url_for("flask-assets.fontawesome", assetpath="css/all.min.css")
    fontawesome_css2 = url_for("flask-assets.fontawesome", assetpath="css/solid.css")
    bootstrap_css = url_for("flask-assets.bootstrap", assetpath="css/bootstrap.min.css")
    bootstrap_js = url_for("flask-assets.bootstrap", assetpath="js/bootstrap.bundle.min.js")
    return f"""
<!doctype html>
<html lang="en">
<head>
  <title> Test Page </title>
  <script src="{htmx}"></script>
  <link href="{fontawesome_css1}", rel="stylesheet" />
  <link href="{fontawesome_css2}", rel="stylesheet" />
  <link href="{bootstrap_css}" rel="stylesheet" />
  <script src="{bootstrap_js}"></script>
</head>
<body class="container-fluid">
  <h1> Test Page </h1>

  <p>This page has htmx, bootstrap, and fontawesome loaded</p>
</body>
</html>
"""
