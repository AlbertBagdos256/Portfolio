from flask_fontawesome import FontAwesome
from blog.config import Config
from flask import Flask

from blog.models import bcrypt
from blog.models import login_manager
from blog.models import db
from blog.users.routes import users
from blog.posts.routes import posts
from blog.main.routes import main





def create_app(config_class = Config):
    # init app
    app = Flask(__name__)
    fa = FontAwesome(app)
    app.config.from_object(Config)
    
    # database and login system
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    
    return app


