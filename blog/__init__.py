from flask_sqlalchemy import SQLAlchemy
from flask_fontawesome import FontAwesome
from blog.config import Configuration
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
fa = FontAwesome(app)
app.config.from_object(Configuration)

# Databse
app.secret_key = 'hn23Lop3781456gs8ghr74yr8hh73ABH789y83fGn23hBJOP123DBGshAlolHjU762FRhjhvcb3738yyfgb3fhif74uibuy8huibfh8yug8ihf8j389unhhf8u8'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
SQLAlCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from blog import routes
