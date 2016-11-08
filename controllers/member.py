from flask import Blueprint, render_template, request

member_view = Blueprint('member_view', __name__)

@member_view.route('/index')
@member_view.route('/')
def index():
  return render_template('index.jade')