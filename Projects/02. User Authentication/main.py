'''PYCODE | @_py.code'''

# > The Flask
# > Project - 02

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(server)

class User(db.Model):
    id = db.Column(db.String, primary_key = True)
    username = db.Column(db.String, primary_key = False)
    password = db.Column(db.String, primary_key = False)
    
    def __repr__(self):
        return f"Id: {self.id} | Username: {self.username}"
    
@server.route('/')
def index():
    return render_template('index.html')

@server.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(id=str(uuid4()), username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return f"User {username} logged in"
    else:
        return render_template('index.html')
    
@server.route('/users')
def showUser():
    users = User.query.all()
    return render_template('users.html', users=users)
    
if __name__ == "__main__":
    server.run()