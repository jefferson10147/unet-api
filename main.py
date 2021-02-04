from app import created_app


app = created_app()

@app.route('/')
def hello_world():
    return 'Hello, World hey!'
