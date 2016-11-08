# coding: utf-8
from flask import Blueprint, render_template, request, jsonify
from models.user_model import User

admin_view = Blueprint('admin_view', __name__)

@admin_view.route('/')
def index():
  return render_template('admin/index.jade', data = {'a': 123})
@admin_view.route('/fetch_users')
def fetch_users():
  return jsonify({'status': 0, 'data': None})
@admin_view.route('/create_user')
def create_user():
  return request.query