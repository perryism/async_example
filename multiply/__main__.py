from flask import Flask, request
from quaff import quaff
from quaff.strategies import FlaskEndpoint
import time

flask_app = Flask(__name__)

def multiply(x, y):
    return x * y

# It auto-generates a simple form
@quaff(FlaskEndpoint(flask_app, "/multiply"))
def multiply_api(y: int, x: int, sleep: int= 0):
    time.sleep(sleep)
    return multiply(x, y)

flask_app.run(host = '0.0.0.0',port=5556)
