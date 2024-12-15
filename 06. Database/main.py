'''PYCODE | @_py.code'''

# > The Flask
# > 06. Database

# & Install Flask SQLAlchemy: pip install flask_sqlalchemy

# ? Importing Required Libraries
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

# ? Configuring Server and Database
server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(server)

# ? Defining Model
class User(db.Model):
    user_id = db.Column(db.String, primary_key = True)
    username = db.Column(db.String, primary_key = True)
    password = db.Column(db.String, primary_key = True)
    
    def __repr__(self):
        return f"User: {self.user_id}: {self.username} - {self.password}"
    
# * Base Route
@server.route('/')
def index():
    db.create_all()
    return render_template('index.html')

# * Add Route
@server.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(user_id=str(uuid4()), username=username, password=password)
        db.session.add(new_user) # Add data to db
        db.session.commit() # Save changes
        return f"User {username} added successfully!"
    else:
        return render_template('index.html')
    
# * Query Route: To query all data in DB
@server.route('/show')
def show():
    users = User.query.all()
    print(users)
    return 'All users are displayed one the console'

# * Udate Route: To update a record
@server.route('/update')
def update():
    user = User.query.filter_by(username="Alice")
    if user:
        user.user_id = "XXXX-1124"
        db.session.commit()
        return "User Updated"
    else:
        return "Can't Find User"
    
# * Delete Route: To delete a record
@server.route('/delete')
def delete():
    user = User.query.filter_by(username="Alice").first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return "User Deleted"
    else:
        return "Can't Find User"

# ? Running the App
if __name__ == "__main__":
    server.run(debug=True)
