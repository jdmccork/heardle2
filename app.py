from flask import Flask

def create_app():
    app = Flask(__name__)

    from apps.hello import hello
    app.register_blueprint(hello)

    return app
