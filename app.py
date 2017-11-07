import os
from bottle import *

@route('/')
def index():
  return "Hallo Heroku!"
 
run(host='0.0.0.0', port=os.environ.get('PORT'))
