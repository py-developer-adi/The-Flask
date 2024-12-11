'''PYCODE | @_py.code'''

# > The Flask
# > 03. The First Step

# ? Server
from flask import Flask, redirect, url_for
server = Flask(__name__)

# ? Routing
@server.route('/')
def index():
    return "Index Page"

# route decorator to bind a function with a URL
@server.route('/hello')

# function to bind with the URL
def hello():
    return "Hello, Flask"

# ? Dynamic URL
@server.route('/blogs/<blog_post>')
def showBlog(blog_post):
    return f"{blog_post} Content"

# ? URL Building
@server.route('/admin')
def logAdmin():
    return "Admin Page"

@server.route('/guest/<guest>')
def logGuest(guest):
    return f"Hello, {guest}, Welcome to Guest Page"

@server.route('/user/<user>')
def showUser(user):
    if user == 'admin':
        return redirect(url_for('logAdmin'))
    else:
        return redirect(url_for('logGuest', guest=user))
    
if __name__ == "__main__":
    server.run()
