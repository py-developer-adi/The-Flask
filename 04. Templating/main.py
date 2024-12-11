'''PYCODE | @_py.code'''

# > The Flask
# > 04. Templating

# * Server
from flask import Flask, render_template
server = Flask(__name__)

@server.route('/')
def index():
    return render_template('index.html')

@server.route('/blogs')
def showBlog():
    return render_template('/blogs/blog1.html')


if __name__ == "__main__":
    server.run(debug=True)
