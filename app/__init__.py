from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from dotenv import load_dotenv

App = Flask(__name__)
App.config.from_object(Config)
db = SQLAlchemy(App, session_options={"autoflush": False})
migrate = Migrate(App, db)
db.init_app(App)

from app import routes, models
