import os

from flask import Flask
import game

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.register_blueprint(game.bp)

    return app

app = create_app()