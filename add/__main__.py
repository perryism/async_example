from flask import Flask, request
from quaff import quaff
from quaff.strategies import FlaskEndpoint
import time

flask_app = Flask(__name__)

def add(x, y):
    return x + y

# It auto-generates a simple form
@quaff(FlaskEndpoint(flask_app, "/add"))
def add_api(y: int, x: int, sleep: int = 0):
    time.sleep(sleep)
    return add(x, y)

flask_app.run(host = '0.0.0.0',port=5555)
