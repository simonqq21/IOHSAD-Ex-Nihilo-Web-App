from flask import render_template, url_for, request, jsonify, send_from_directory
from app import App
from datetime import datetime, date
import os
import re

@App.route('/', methods=['GET'])
@App.route('/index', methods=['GET'])
def index():
    return render_template('index.html')