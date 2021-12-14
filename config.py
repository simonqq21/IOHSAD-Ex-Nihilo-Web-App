import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "iohsadexnihilo"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    "postgresql+psycopg2://simonque:12345678@localhost/swengdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
