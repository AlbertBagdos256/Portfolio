from flask import render_template, request, Blueprint
from blog.models import User
from blog.main.utils import get_users_urls,get_users_avatars,get_main_list

main = Blueprint('main', __name__)

@main.route('/', methods = ['POST','GET'])
def index():
    users = User.query.all()
    images_list = get_users_avatars(users)
    users_urls  = get_users_urls(users)
    main_list   = get_main_list(images_list, users_urls)
    return render_template('index.html', main_list = main_list) 
