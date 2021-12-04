from flask import render_template, url_for, request, jsonify, send_from_directory

from app import App
from datetime import datetime, date
import os
import re

'''
route for index page
'''
@App.route('/', methods=['GET'])
@App.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

'''
route for forms
formname parameter is the short name of the form
'''
@App.route('/forms/<formname>', methods=['GET'])
def renderForm(formname):
    return render_template(f"{formname}.html")
