# coding: utf-8
from flask import Flask, render_template, request
import leancloud, time
from StringIO import StringIO

from controllers.member import member_view
from controllers.admin import admin_view

app = Flask(__name__, static_folder = 'assets', template_folder = 'views')
app.jinja_env.variable_start_string = '[['
app.jinja_env.variable_end_string = ']]'
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

# 动态路由url_prefix
app.register_blueprint(admin_view, url_prefix = '/admin')
app.register_blueprint(member_view, url_prefix = '/user')


@app.route('/')
def index():
  return render_template('index.jade')

@app.route('/upload_file', methods = ['POST'])
def upload_file():
  fn = str(int(time.time() * 1000)) + ".jpg"
  io = StringIO()
  io.write(request.files['file'].read())
  file = leancloud.File(fn, io)
  file.save()
  io.close()
  return '{"status": 0, "url": "%s", "id": "%s"}'%(file.url, file.id)
