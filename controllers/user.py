from flask import Blueprint, render_template

user = Blueprint('user', __name__)

@user.route('/index')
@user.route('/')
def index():
  return render_template('index.jade')