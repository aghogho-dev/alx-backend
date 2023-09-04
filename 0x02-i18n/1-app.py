#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    default_locale = "en"
    timezone = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@app.route('/', strict_slashes=False)
def index() -> str:
    """Renders HTML template"""
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run()
