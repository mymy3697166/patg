# coding: utf-8
from flask import Blueprint, render_template, request, jsonify
from models.member import Member

admin_view = Blueprint('admin_view', __name__)

@admin_view.route('/')
def index():
  return render_template('admin/index.jade', data = {'a': 123})
@admin_view.route('/fetch_users')
def fetch_users():
  rows = 10
  page = 0
  if request.args.has_key('rows'):
    rows = int(request.args['rows'])
  if request.args.has_key('page'):
    page = int(request.args['page'])
  data = Member.fetch_members(page = page, rows = rows)
  return jsonify({'status': 0, 'data': data})
@admin_view.route('/create_user')
def create_user():
  return request.args["abc"]