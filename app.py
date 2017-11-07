import os
from bottle import *

@route('/')
def index():
  return "Well Hello There"
  
run(host='0.0.0.0', port=os.environ.get('PORT'))
