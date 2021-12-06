from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.fields import TelField, EmailField
from wtforms.validators import DataRequired, Email, InputRequired

'''
-Name of Company
-Presence of union (If yes, put down the contact details of the head of the union (contact number and email)
-Contact Details of the one who submitted the form

then finally a large textbox for the nature of the complaint
'''
class ComplaintForm(FlaskForm):
    companyName = StringField("Company Name", validators=[DataRequired(), InputRequired()])
    unionPresence = BooleanField("Union Present", validators=[DataRequired(), InputRequired()])
    unionHeadContactNo = TelField("Union Head Contact No.")
    unionHeadEmail = EmailField("Union Head Email Address", validators=[Email()])
    contactNumber = TelField("Contact No.", validators=[DataRequired(), Email(), InputRequired()])
    complaint = TextAreaField("Enter you complaint here.", validators=[DataRequired(), InputRequired()])
