from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

App = Flask(__name__)
App.config.from_object(Config)

db = SQLAlchemy(App, session_options={"autoflush": False})
migrate = Migrate(App, db)
db.init_app(App)
db.create_all()

login = LoginManager(App)

from app import routes, models
