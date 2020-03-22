# -*- coding: utf-8 -*-

from flask import Flask
from datetime import datetime
from logging import DEBUG
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = b'\xf0z\xbdv\x1d\xf0Y:'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.logger.setLevel(DEBUG)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flask_package import routes