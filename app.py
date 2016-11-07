# coding: utf-8
from flask import Flask
from flask import render_template

# from controllers.todos import todos_view

app = Flask(__name__, static_folder = 'assets', template_folder = 'views')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

# 动态路由url_prefix
# app.register_blueprint(todos_view, ='/todos')


@app.route('/')
def index():
  return render_template('index.jade')
