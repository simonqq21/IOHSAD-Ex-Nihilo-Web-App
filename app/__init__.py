from flask import Flask
from config import Config
# from dotenv import load_dotenv

App = Flask(__name__)
App.config.from_object(Config)
from app import routes
