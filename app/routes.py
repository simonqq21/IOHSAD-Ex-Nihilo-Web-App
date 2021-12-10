from flask import render_template, url_for, request, jsonify, send_from_directory, flash

from app import App
from datetime import datetime, date
from app.db_module import submitForm
from app.forms import ComplaintForm

print(ComplaintForm)
'''
route for index page
'''
@App.route('/', methods=['GET'])
@App.route('/index', methods=['GET'])
def index():
    flash("a")
    return render_template('index.html')
    flash("a")

'''
route for forms
formname parameter is the short name of the form
'''
@App.route('/forms/<formname>', methods=['GET', 'POST'])
def renderForm(formname):
    form = ComplaintForm()
    if request.method == 'POST':
        print(f"Username: {form.username.data}\n \
        Company name: {form.companyName.data}\n \
        Union present: {form.unionPresence.data}\n \
        Union head contact no: {form.unionHeadContactNo.data}\n \
        Union head email address: {form.unionHeadEmail.data}\n \
        Contact number: {form.contactNumber.data}\n \
        Complaint: {form.complaint.data}")

    if form.validate_on_submit():
        flash("Validated")
        flash(f"Username: {form.username.data}\n \
        Company name: {form.companyName.data}\n \
        Union present: {form.unionPresence.data}\n \
        Union head contact no: {form.unionHeadContactNo.data}\n \
        Union head email address: {form.unionHeadEmail.data}\n \
        Contact number: {form.contactNumber.data}\n \
        Complaint: {form.complaint.data}")

        # insert the submission to the database
        username = form.username.data
        questionsAndAnswers = []
        for qa in form:
            if qa.label.field_id not in ("submit", "csrf_token"):
                questionsAndAnswers.append((qa.label.field_id, qa.data))
        print(questionsAndAnswers)
        submitForm(date.today(), username, "Form A", questionsAndAnswers)

    return render_template(f"{formname}.html", title="Complaint Form", form=form)
