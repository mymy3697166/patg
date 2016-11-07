from flask import Blueprint, render_template, request

admin_view = Blueprint('admin_view', __name__)

@admin_view.route('/')
def index():
  return render_template('admin/index.jade')