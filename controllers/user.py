from flask import Blueprint, render_template, request

user_view = Blueprint('user_view', __name__)

@user_view.route('/index')
@user_view.route('/')
def index():
  return render_template('index.jade')