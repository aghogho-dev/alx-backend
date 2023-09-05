#!/usr/bin/env python3
"""Mock logging in"""
from flask import Flask
from flask import g
from flask import request
from flask import render_template
from flaks_label import Babel
from typing import Dict
from typing import Union


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
    loc = request.args.get("locale", "")
    if loc and loc.strip() in Config.LANGUAGES:
        return loc
    return request.accept_languages.best_match(app.config["LANGUAGES"])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """Get user"""
    return user.get(int(id), 0)


@app.before_request
def before_request():
    """Before request"""
    setatrr(g, 'user', get_user(request.args.get('login_as', 0)))


@app.route('/', strict_slashes=False)
def index() -> str:
    """Render HTML template"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
