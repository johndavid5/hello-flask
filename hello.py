from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    sWho = 'index'
    app.logger.debug("%s: Let off some steam, Bennett!"%(sWho))
    return 'Index Page'

@app.route('/hello')
def hello_world():
    sWho = 'hello_world'
    app.logger.debug("%s: Let off some steam, Bennett!"%(sWho))
    return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/projects/')
def projects():
    return 'The "/projects/" folder, Moe...'

@app.route('/about')
def about():
    return 'The "/about" file, Moe...'
