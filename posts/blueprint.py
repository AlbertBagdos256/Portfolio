from flask import Blueprint
from flask import render_template
posts = Blueprint('posts', __name__, template_folder = 'templates')

@posts.route('/')
def Post():
    return render_template('posts/post.html')