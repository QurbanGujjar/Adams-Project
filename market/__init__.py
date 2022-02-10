import bcrypt
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app=Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
app.config['SECRET_KEY']='92c3a79129a1700d77612255'
bcrypt=Bcrypt(app)
# login_manager= LoginManager(app)
from market import views
