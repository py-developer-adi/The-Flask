'''PYCODE | @_py.code'''

# > The Flask
# > 05. Flask Forms

# * Server
from flask import Flask, render_template, request
server = Flask(__name__)

@server.route('/')
def index():
    return render_template('index.html')

@server.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f"{username} logged in with password {password}"
    else:
        return render_template('index.html')

server.run(debug=True)
