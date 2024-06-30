from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config["SECRET_KEY"] = "KrwkqyFK#+HNjk%_!m@xf7PA.+Sqv&"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///DIO.db"

db = SQLAlchemy(app)

login_manager = LoginManager(app)
