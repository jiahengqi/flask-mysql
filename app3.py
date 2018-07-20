from flask import Flask
import time
app = Flask(__name__)
 
@app.route('/')
def index():
    time.sleep(5)
    return '<h1>Hello World</h1>'