import os
import re

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "iohsadexnihilo"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or "postgresql+psycopg2://simonque:12345678@localhost/swengdb"  # or other relevant config var
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)


    SQLALCHEMY_TRACK_MODIFICATIONS = False
