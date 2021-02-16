from flask import render_template
from flask.helpers import get_debug_flag

from app import create_app
from app.settings import Development, Config


config = Development if get_debug_flag() else Config
app = create_app(config)
