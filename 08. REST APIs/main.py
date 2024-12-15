'''PYCODE | @_py.code'''

# > The Flask
# > 08. REST APIs

# * Server
from flask import Flask, jsonify # ? jsonify to return json data
import json

server = Flask(__name__)

# | Base Route
@server.route('/')
def index():
    return jsonify({
        "Response": "Hello World"
    })
    
# ? Sample Data
with open(f"data.json", 'r') as f:
    data = json.load(f)
    
@server.route('/data')
def showdata():
    return jsonify(data)
