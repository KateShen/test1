
from flask import Flask
app = Flask(__name__)

from datetime import datetime
now = datetime.now()

import time

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/currentTime')
def hello1():
 	return now.strftime("%Y-%m-%d")

@app.route('/currentTime/timeZone')
def hello2():
  	return time.tzname[time.daylight]