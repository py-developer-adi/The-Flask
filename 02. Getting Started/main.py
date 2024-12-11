'''PYCODE | @_py.code'''

# > The Flask
# > 02. Setup & Installation

from flask import Flask
server = Flask(__name__)

@server.route('/')
def index():
    return "Hello, Flask"

# server.run(debug=True, host="0.0.0.0")
