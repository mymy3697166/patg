# coding: utf-8
from flask import Flask
from flask import render_template

from controllers.user import user_view
from controllers.admin import admin_view

app = Flask(__name__, static_folder = 'assets', template_folder = 'views')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

# 动态路由url_prefix
app.register_blueprint(admin_view, url_prefix = '/admin')
app.register_blueprint(user_view, url_prefix = '/user')


@app.route('/')
def index():
  return render_template('index.jade')
