from flask import render_template
from flask.helpers import get_debug_flag

from app import created_app
from app.settings import Development, Production


config = Development if get_debug_flag() else Production
app = created_app(config)


@app.route('/')
def hello_world():
    return render_template("index.html")
