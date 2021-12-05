from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TelField, EmailField, TextAreaField
from wtforms.validators import DataRequired

'''
-Name of Company
-Presence of union (If yes, put down the contact details of the head of the union (contact number and email)
-Contact Details of the one who submitted the form

then finally a large textbox for the nature of the complaint
'''
class ComplaintForm(FlaskForm):
    companyName = StringField("Company Name", validators=[DataRequired()])
    unionPresence = BooleanField()
    unionHeadContactNo = TelField()
    unionHeadEmail = EmailField()
    contactNumber = TelField()
    complaint = TextAreaField()
