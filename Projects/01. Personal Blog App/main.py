'''PYCODE | @_py.code'''

# > The Flask
# > Project - 01

from flask import Flask, render_template

server = Flask(__name__)

# Sample blog data
posts = [
    {
        'id': 1,
        'title': 'First Blog Post',
        'summary': 'This is a summary of the first post.',
        'content': 'This is the full content of the first blog post.',
        'author': 'John Doe',
        'date': 'December 15, 2024',
    },
    {
        'id': 2,
        'title': 'Second Blog Post',
        'summary': 'This is a summary of the second post.',
        'content': 'This is the full content of the second blog post.',
        'author': 'Jane Doe',
        'date': 'December 16, 2024',
    },
]

@server.route('/')
def index():
    return render_template('index.html', posts=posts)

@server.route('/blog/<int:blog_id>')
def showBlog(blog_id):
    post = next((p for p in posts if p['id'] == blog_id), None)
    if not post:
        return "Post Not Found", 404
    return render_template('blog.html', post=post)

if __name__ == "__main__":
    server.run()