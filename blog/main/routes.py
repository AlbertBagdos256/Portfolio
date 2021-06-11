from flask import render_template, request, Blueprint

main = Blueprint('main', __name__)

@main.route('/', methods = ['POST','GET'])
def index():
    return render_template('index.html')  
