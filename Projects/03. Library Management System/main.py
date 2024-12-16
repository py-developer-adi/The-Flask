'''PYCODE | @_py.code'''

# > The Flask
# > Project - 03

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
server.config['SQLALCHEMY_TRACK_MODIFICATONS'] = False
db = SQLAlchemy(server)

class Books(db.Model):
    id = db.Column(db.String, primary_key = True)
    title = db.Column(db.String, primary_key = False)
    author = db.Column(db.String, primary_key = False)
    
    def __repr__(self):
        return f"Id: {self.id} | Title: {self.title}"
    
@server.route('/')
def index():
    books = Books.query.all()
    return render_template('index.html', books=books)

@server.route('/add')
def add():
    return render_template('new.html', doc={"title": "New Book"})

@server.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        new_book = Books(id=str(uuid4()), title=title, author=author)
        db.session.add(new_book)
        db.session.commit()
    return render_template('index.html')

@server.route('/delete')
def delete():
    return render_template('delete.html', doc={"title": "Delete Book"})

@server.route('/remove', methods=['GET', 'POST'])
def remove():
    if request.method == 'POST':
        title = request.form['title']
        book = Books.query.filter_by(title=title).first()
        if book:
            db.session.delete(book)
            db.session.commit()
            return "Book Deleted"
        else:
            return "Book Not Found", 404
    return render_template('index.html')

if __name__ == "__main__":
    server.run(debug=True)