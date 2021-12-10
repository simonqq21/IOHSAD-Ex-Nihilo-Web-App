from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.fields.html5 import TelField, EmailField
from wtforms.validators import DataRequired, Email, InputRequired, Optional

'''
-Name of Company
-Presence of union (If yes, put down the contact details of the head of the union (contact number and email)
-Contact Details of the one who submitted the form

then finally a large textbox for the nature of the complaint
'''
class ComplaintForm(FlaskForm):
    username = StringField("Unique Username*", validators=[DataRequired(), InputRequired()])
    companyName = StringField("Company Name* (Pangngalan ng kumpanya)*", validators=[DataRequired(), InputRequired()])
    unionPresence = BooleanField("Union Present* (Mayroon bang unyon ng mga manggagawa?)*")
    unionHeadContactNo = TelField("Union Head Contact No. (Telepono ng pinuno ng unyon ng mga manggagawa)", validators=[Optional()])
    unionHeadEmail = EmailField("Union Head Email Address (Email address ng pinuno ng unyon ng mga manggagawa)", validators=[Email(), Optional()])
    emailPhone = StringField("Contact No. / Email Address* (Telepono / Email Address)*", validators=[DataRequired(), InputRequired()])
    complaint = TextAreaField("Enter you complaint here* (I-type ang inyong reklamo dito*)", validators=[DataRequired(), InputRequired()])
    submit = SubmitField("Submit Form (Ipasa ang form)")
