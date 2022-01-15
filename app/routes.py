from flask import redirect, render_template, url_for, request, jsonify, send_from_directory, flash

from app import App
from datetime import datetime, date
from app.models import submitForm, User, Administrator
from app.forms import AdminLoginForm
from app.forms import ComplaintForm, COVID19Survey

from sqlalchemy import or_

from flask_login import current_user, login_user

'''
route for index page
'''
@App.route('/', methods=['GET'])
@App.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

# '''
# route for administrator signup page
# '''
# @app.route('/admin', methods=['GET', 'POST'])
# def login():
#     pass

'''
route for administrator login page
'''
@App.route('/admin', methods=['GET', 'POST'])
def adminlogin():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = AdminLoginForm
    if form.validate_on_submit():
        admin = Administrator.query.filter_by(or_(username=form.emailusername.data, email=form.emailusername.data)).first()
        if admin is None or not admin.check_password_hash(form.password.data):
            flash('Invalid username or password.')
            return redirect(url_for('adminlogin'))
        login_user(admin, remember = form.remember_me.data)
        return redirect(url_for('index'))
    # return render_template()

'''
route for administrator logout page
'''
@App.route('/logout', methods=['GET', 'POST'])
def adminlogout():
    pass

'''
route for administrative view page
'''
@App.route('/adminview', methods=['GET', 'POST'])
def adminview():
    pass

'''
route for forms
formname parameter is the short name of the form
'''
@App.route('/forms/<formname>', methods=['GET', 'POST'])
def renderForm(formname):
    print(formname)
    if formname == "forma":
        form = ComplaintForm()
    elif formname == "COVID19Survey":
        form = COVID19Survey()

    if request.method == 'POST':
        print(f"Username: {form.username.data}\n \
        Company name: {form.companyName.data}\n \
        Union present: {form.unionPresence.data}\n \
        Union head contact no: {form.unionHeadContactNo.data}\n \
        Union head email address: {form.unionHeadEmail.data}\n \
        Contact number: {form.emailPhone.data}\n \
        Complaint: {form.complaint.data}")

    if form.validate_on_submit():
        # flash("Validated")
        # flash(f"Username: {form.username.data}\n \
        # Company name: {form.companyName.data}\n \
        # Union present: {form.unionPresence.data}\n \
        # Union head contact no: {form.unionHeadContactNo.data}\n \
        # Union head email address: {form.unionHeadEmail.data}\n \
        # Contact number: {form.emailPhone.data}\n \
        # Complaint: {form.complaint.data}")

        # insert the submission to the database
        username = form.username.data
        emailPhone = form.emailPhone.data
        questionsAndAnswers = []
        for qa in form:
            # ignore the submit and csrf token fields
            if qa.label.field_id not in ("submit", "csrf_token"):
                questionsAndAnswers.append((qa.label.field_id, qa.data))
        print(questionsAndAnswers)
        submitForm(date.today(), (username, emailPhone), "Form A", questionsAndAnswers)
        flash("Your form has been submitted. ")
        return redirect(url_for('index'))

    return render_template(f"{formname}.html", title="Complaint Form", form=form)

#@App.route('/uniqueUsername', methods=['GET'])
#def checkUsername():
#    args = request.args
#    User.username
#    return 1
