![version](https://img.shields.io/badge/version-0.3.0-blue)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
![GitHub last commit](https://img.shields.io/github/last-commit/garzola/flask-assets)
![Coverage Status](./reports/coverage/coverage-badge.svg)
<!-- ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/garzola/flask-assets) -->
<!-- ![GitHub Release Date](https://img.shields.io/github/release-date/garzola/flask-assets) -->
<!-- ![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/garzola/flask-assets/total) -->


<hr />

# flask-assets

Flask-assets provides a convenient way to add the following frameworks to your Flask application:

* Bootstrap 5.3.3
* htmx 2.0.4
* Font Awesome 6.7.2
* Tom-Select 2.4.1

## Installing with Poetry

```
poetry add git+ssh://git@https://github.com/garzola/flask-assets.git
```

## Using

The following is a very basic example of referencing the assets in this package.  `url_for()` is also available in Jinja templates and used the same way.

```python
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
    tom_select_js = url_for("flask-assets.tom-select", assetpath="tom-select.complete.js")
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
```

The code snippet is not located within the flask-assets package.  You can find this code in the root of the github repo under the name `testsrv.py`


## Linking to htmx files
You can find information about htmx at [https://htmx.org](https://htmx.org)

```python
url_for("flask-assets.htmx", assetpath="htmx.min.js")
```

## Linking to Fontawesome files
You can find information about fontawesome at [https://fontawesome.com](https://fontawesome.com)

```python
url_for("flask-assets.fontawesome", assetpath="css/all.min.css")
url_for("flask-assets.fontawesome", assetpath="css/solid.css")
```

## Linking to Bootstrap files
You can find information about bootstrap at [getbootstrap.com](https://getbootstrap.com)

```python
url_for("flask-assets.bootstrap", assetpath="css/bootstrap.min.css")
url_for("flask-assets.bootstrap", assetpath="js/bootstrap.bundle.min.js")
```

## Linking to tom-select.js files
You can find information about tom-select.js at [tom-select.js.org](https://tom-select.js.org)

```python
url_for("flask-assets.tom-select", assetpath="tom-select.complete.js")
```
