import os
from flask import Flask
from flask_socketio import SocketIO
from flask_mysqldb import MySQL

socketio = SocketIO()

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
    app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
    app.config['MYSQL_DB'] = 'flask'


    app.secret_key = os.environ.get('SECRET_KEY')

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app

app = create_app()
mysql = MySQL(app)