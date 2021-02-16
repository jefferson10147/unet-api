from flask import render_template
from flask.helpers import get_debug_flag

from app import created_app
from app.settings import Development, Config


config = Development if get_debug_flag() else Config
app = created_app(config)
