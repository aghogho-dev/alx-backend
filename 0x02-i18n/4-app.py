#!/usr/bin/env python3
"""Get locale from request"""
from flask import Flask
from flask import request
from flask import render_template
from flask_babel import Babel


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCALE = "en"
    DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get locale"""
    loc = request.args.get('locale', None)
    if loc and loc in Config.LANGUAGES:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """Render HTML template"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
