# coding: utf-8
from flask import Blueprint, render_template, request, jsonify
from models.member import Member
import math

admin_view = Blueprint('admin_view', __name__)

@admin_view.route('/')
def index():
  return render_template('admin/index.jade', data = {'a': 123})

@admin_view.route('/fetch_members')
def fetch_members():
  rows = 10
  page = 0
  if request.args.has_key('rows'):
    rows = int(request.args['rows'])
  if request.args.has_key('page'):
    page = int(request.args['page'])
  data = Member.fetch_members(page = page, rows = rows)
  return jsonify({'status': 0, 'data': data, 'count': Member.query.count()})

@admin_view.route('/update_member', methods = ['POST'])
def update_member():
  Member.update_member(
    id = request.json['id'],
    phone = request.json['phone'],
    email = request.json['email'],
    name = request.json['name'],
    gender = request.json['gender'],
    dob = request.json['dob'],
    avatar = request.json['avatar'],
    signature = request.json['signature'],
    description = request.json['description'],
    status = request.json['status']
  )
  return jsonify({'status': 0})