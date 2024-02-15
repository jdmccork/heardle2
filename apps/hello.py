from flask import Blueprint, render_template

hello = Blueprint('hello', __name__)

@hello.route('/hello')
def index():
    return render_template('hello.html')