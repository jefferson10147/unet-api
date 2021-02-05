from flask.helpers import get_debug_flag

from app import created_app
from app.settings import Development


if get_debug_flag():
    config = Development

app = created_app(config)


@app.route('/')
def hello_world():
    return 'Hello, World hey! im in debug mode with db'
