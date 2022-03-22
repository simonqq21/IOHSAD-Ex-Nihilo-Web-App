from app import db
from datetime import date
from sqlalchemy.orm import aliased
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from sqlalchemy import or_, and_

# forms table class
class Form(db.Model):
    __tablename__ = 'Form'
    id = db.Column(db.Integer, primary_key=True)
    form_name = db.Column(db.String, unique=True)

    questions = db.relationship("Question", back_populates="form", cascade="all, delete, delete-orphan")
    submissions = db.relationship("Submission", back_populates="form", cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"Form(id={self.id!r}, form_name={self.form_name!r})"

# questions table class
class Question(db.Model):
    __tablename__ = 'Question'
    id = db.Column(db.Integer, primary_key = True)
    form_id = db.Column(db.ForeignKey('Form.id'))
    short_name = db.Column(db.String)

    form_question = db.UniqueConstraint(form_id, short_name, name="form_question")
    form = db.relationship("Form", back_populates="questions")
    answers = db.relationship("Answer", back_populates="question", cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"Question(id={self.id!r}, form_id={self.form_id!r}, short_name={self.short_name!r})"

# submissions table class
class Submission(db.Model):
    __tablename__ = 'Submission'
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date, nullable=False, default=date.today())
    user_id = db.Column(db.ForeignKey("User.id"), nullable=False)
    form_type = db.Column(db.ForeignKey('Form.id'), nullable=False)

    # user_form = UniqueConstraint(user_id, form_type, name="user_form")
    form = db.relationship("Form", back_populates="submissions")
    user = db.relationship("User", back_populates="submissions")
    answers = db.relationship("Answer", back_populates="submission", cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"Submission(id={self.id!r}, date={self.date!r}, user_id={self.user_id!r}, \
            form_type={self.form_type!r})"

# users table class
class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True)
    contactNumber = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True)

    submissions = db.relationship("Submission", back_populates="user", cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id!r}, username={self.username!r})"

    def check_unique_username(newUsername):
        if User.query.filter_by(username = str(newUsername).first()):
            return 0
        else:
            return 1

# administrators class
class Administrator(UserMixin, db.Model):
    __tablename__ = 'Administrator'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False, index=True, unique=True)
    email = db.Column(db.String(120), nullable=False, index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"Administrator(username={self.username!r}, email={self.email!r})"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_admin(id):
    return Administrator.query.get(int(id))

# answers table class
class Answer(db.Model):
    __tablename__ = 'Answer'
    id = db.Column(db.Integer, primary_key=True)
    submission_id = db.Column(db.ForeignKey("Submission.id"))
    question_id = db.Column(db.ForeignKey('Question.id'))
    answer_string = db.Column(db.String)

    submission = db.relationship("Submission", back_populates="answers")
    question = db.relationship("Question", back_populates="answers")

    def __repr__(self):
        return f"Answer(submission_id={self.submission_id!r}, question_id={self.question_id!r}, \
            answer_string={self.answer_string!r})"

# uncomment to drop all tables, for testing only
# try:
#     db.engine.execute('''DROP TABLE "User" CASCADE''')
# except Exception as err:
#     print(err)
#     pass
# try:
#     db.engine.execute('DROP TABLE "Question" CASCADE')
# except Exception as err:
#     print(err)
#     pass
# try:
#     db.engine.execute('DROP TABLE "Submission" CASCADE')
# except Exception as err:
#     print(err)
#     pass
# try:
#     db.engine.execute('DROP TABLE "Form" CASCADE')
# except Exception as err:
#     print(err)
#     pass
# try:
#     db.engine.execute('DROP TABLE "Answer" CASCADE')
# except Exception as err:
#     print(err)
#     pass

db.create_all()
# uncomment to drop all tables, for testing only
# db.drop_all()

def commit():
    try:
        db.session.commit()
    except Exception as err:
        print(type(err))
        # print(err)
        db.session.rollback()
        db.session.close()

def query(alias):
    items = []
    for instance in db.session.query(alias):
        items.append(instance)
    print(items)


# define table aliases
f = aliased(Form, name='f')
q = aliased(Question, name='q')
s = aliased(Submission, name='s')
u = aliased(User, name='u')
a = aliased(Answer, name='a')


'''
method to insert new form with a set of questions
If the form exists
form_name (string) - form name
questions (list of strings) - the list of short question names
'''
def insertForm(formName, questions):
    newForm = Form(form_name=formName)
    db.session.add(newForm)
    commit()
    for question in questions:
        newForm.questions.append(Question(short_name=question))
        commit()

'''
method to select all forms that currently exist in the database.
'''
def selectAllFormNames():
    formnames = []
    for instance in db.session.query(f):
        formnames.append(instance)
    return formnames

'''
method to select a single form given a keyword string
Questions can be accessed from the form using the questions attribute of the form.
formNameLike (string) - form name search string wildcard
'''
def selectForm(formNameLike):
    form = db.session.query(f).where(f.form_name.like(f"%{formNameLike}%")).first()
    return form

'''
method to rename a form
oldFormName (string)
newFormName (string)
'''
def renameForm(oldFormName, newFormName):
    form = db.session.query(f).where(f.form_name.like(f"{oldFormName}")).first()
    if form is not None:
        form.form_name = newFormName
        commit()

'''
method to add a question to a form that exists
formName (string) - exact name of form
questionShortNames (list of string) - list of question short names
'''
def addQuestionsToForm(formName, questionShortNames):
    form = db.session.query(f).where(f.form_name.like(formName)).first()
    if form is not None:
        for name in questionShortNames:
            try:
                form.questions.append(Question(short_name=name))
                commit()
            except Exception as err:
                print(err)
                print(type(err))


'''
method to remove a question from a form that exists
formName (string) - exact name of form
questionShortNames (list of string) - list of question short names
'''
def deleteQuestions(formName, questionShortNames):
    fId = db.session.query(f.id).where(f.form_name.like(formName)).first()[0]
    print(fId)
    for name in questionShortNames:
        question = db.session.query(q).where(and_(q.short_name.like(name), q.form_id == fId)).first()
        if question is not None:
            db.session.delete(question)
            commit()

'''
method to delete a form together with all its questions
'''
def deleteForm(formName):
    form = db.session.query(f).where(f.form_name.like(f"{formName}")).first()
    if form is not None:
        db.session.delete(form)
        commit()

'''
method to insert a form submission together with the user and all answers
date (date) - date submitted
user (tuple of string) - user represented by tuple (<username>, <contactNumber>)
formname (string) - form name
questionsAndAnswers (list of tuples) - list of tuples containing the question short name and answer
'''
def submitForm(submitDate, user, formName, questionsAndAnswers):
    submission = Submission()
    submission.date = submitDate
    username = user[0]
    contactNumber = user[1]
    user = db.session.query(u).where(u.username.like(username)).first()
    if user is None:
        user = User(username=username, contactNumber=contactNumber)
        db.session.add(user)
        commit()
    submission.user = user
    form = db.session.query(f).where(f.form_name.like(formName)).first()
    if form is not None:
        submission.form = form

        for qa in questionsAndAnswers:
            # question = db.session.query(q).where(and_(q.short_name.like(qa[0]), q.form_id == form.id)).first()
            question = db.session.query(q).where(and_(q.short_name.like(qa[0]), q.form_id == submission.form.id)).first()
            if question is not None:
                answer = Answer(answer_string = qa[1], question=question)
                submission.answers.append(answer)

        db.session.add(submission)
        commit()

# insert forms A and B
formnames = []
generalComplaintForms = ["accidentalInjuryForm",
                        "accidentalDeathForm",
                        "OSHViolationForm",
                        "nonCompensationForm"]
for formname in generalComplaintForms:
    formnames.append(formname)
formnames.append("COVID19Survey")
# formnames.append("Form B")

# insert questions
questions = {}
# questions for complaintForm
for formname in generalComplaintForms:
    questions[formname] = []
# questions["complaintForm"].append("name")
# questions["complaintForm"].append("age")
# questions["complaintForm"].append("sex")
# questions["complaintForm"].append("civilStatus")
# questions["complaintForm"].append( "education")
# questions["complaintForm"].append("position")
# questions["complaintForm"].append("yearsWorked")
# questions["complaintForm"].append("workStatus")
# questions["complaintForm"].append("wage")
# questions["complaintForm"].append("benefits")
# questions["complaintForm"].append("benefitsReceived")
# questions["complaintForm"].append("hoursPerDay")
# questions["complaintForm"].append("chemicalUse")
# questions["complaintForm"].append("chemicalName")
# questions["complaintForm"].append("chemicalPurpose")
# questions["complaintForm"].append("chemExposureDuration")
# questions["complaintForm"].append("diseaseAccidented")
# questions["complaintForm"].append("treatmentBillSource")
# questions["complaintForm"].append("treatmentLocation")
# questions["complaintForm"].append("reproductiveProblem")
# questions["complaintForm"].append("knowOthersSickAccidented")
# questions["complaintForm"].append("yearlyPhysicalExamination")
# questions["complaintForm"].append("workPPE")
# questions["complaintForm"].append("workPPEFree")
# questions["complaintForm"].append("workHazards")
# questions["complaintForm"].append("wasteDisposal")
# questions["complaintForm"].append("DOLEInspection")
# questions["complaintForm"].append("safetyOfficerPresent")

# questions for Form B
# questions["Form B"] = []
# questions["Form B"].append("name")
# questions["Form B"].append("address")
# questions["Form B"].append("age")
# questions["Form B"].append("sex")
# questions["Form B"].append("civilStatus")
# questions["Form B"].append("occupation")
# questions["Form B"].append("employingCompanyName")
# questions["Form B"].append("chiefComplaint")
# questions["Form B"].append("presentMedicalHistory")
# questions["Form B"].append("pastMedicalHistory")
# questions["Form B"].append("pastPersonalHistory")
# questions["Form B"].append("familyMedicalHistory")
# questions["Form B"].append("pastJob")
# questions["Form B"].append("pastJobDuration")
# questions["Form B"].append("currentJob")
# questions["Form B"].append("currentJobSection")
# questions["Form B"].append("currentJobDuration")
# questions["Form B"].append("currentJobDescription")
# questions["Form B"].append("currentJobHazards")
# questions["Form B"].append("medicalHistorySHEENT")
# questions["Form B"].append("medicalHistoryRespiratory")
# questions["Form B"].append("medicalHistoryCirculatory")
# questions["Form B"].append("medicalHistoryDigestive")
# questions["Form B"].append("medicalHistoryUrogenital")
# questions["Form B"].append("medicalHistoryEndocrine")
# questions["Form B"].append("medicalHistoryNervous")
# questions["Form B"].append("medicalHistoryMusculoskeletal")
# questions["Form B"].append("vitalSignBP")
# questions["Form B"].append("vitalSignPR")
# questions["Form B"].append("vitalSignTemp")
# questions["Form B"].append("vitalSignWeight")
# questions["Form B"].append("generalAppearance")
# questions["Form B"].append("physicalExaminationSHEENT")
# questions["Form B"].append("physicalExaminationLungs")
# questions["Form B"].append("physicalExaminationHeart")
# questions["Form B"].append("physicalExaminationAbdomen")
# questions["Form B"].append("physicalExaminationExtremities")
# questions["Form B"].append("diagnosis")
# questions["Form B"].append("management")

questions["COVID19Survey"] = []
questions["COVID19Survey"].append("username")
questions["COVID19Survey"].append("contactNumber")
questions["COVID19Survey"].append("fullname")
questions["COVID19Survey"].append("shiftdate")
questions["COVID19Survey"].append("shifttime")
questions["COVID19Survey"].append("fever")
questions["COVID19Survey"].append("coughcolds")
questions["COVID19Survey"].append("bodypain")
questions["COVID19Survey"].append("sorethroat")
questions["COVID19Survey"].append("contact")
questions["COVID19Survey"].append("directcare")
questions["COVID19Survey"].append("internationalTravel")
questions["COVID19Survey"].append("domesticTravel")
questions["COVID19Survey"].append("domesticTravelDetails")
questions["COVID19Survey"].append("complaint")
# questions["COVID19Survey"].append("username")
# questions["COVID19Survey"].append("contactNumber")
# questions["COVID19Survey"].append("email")
# questions["COVID19Survey"].append("companyName")
# questions["COVID19Survey"].append("companyLocation")
# questions["COVID19Survey"].append("freeMassTesting")
# questions["COVID19Survey"].append("freeMassTestingDetails")
# questions["COVID19Survey"].append("dailyHealthMonitoring")
# questions["COVID19Survey"].append("distancing")
# questions["COVID19Survey"].append("distancingHardToImplementArea")
# questions["COVID19Survey"].append("supplements")
# questions["COVID19Survey"].append("supplementList")
# questions["COVID19Survey"].append("mhprograms")
# questions["COVID19Survey"].append("freePPE")
# questions["COVID19Survey"].append("freePPEDetails")
# questions["COVID19Survey"].append("adequateSoapAndWater")
# questions["COVID19Survey"].append("freeRubbingAlcohol")
# questions["COVID19Survey"].append("regularDisinfection")
# questions["COVID19Survey"].append("hoursPerDay")
# questions["COVID19Survey"].append("overtime")
# questions["COVID19Survey"].append("covidInformationCampaign")
# questions["COVID19Survey"].append("covidInformationCampaignDetails")
# questions["COVID19Survey"].append("freeSafeTransportation")
# questions["COVID19Survey"].append("freeSafeTransportationDetails")
# questions["COVID19Survey"].append("freeSafeAccomodation")
# questions["COVID19Survey"].append("freeSafeAccomodationDetails")
# questions["COVID19Survey"].append("freeMedicalCheckup")
# questions["COVID19Survey"].append("covidRiskAssessment")
# questions["COVID19Survey"].append("isolationRoomPresent")
# questions["COVID19Survey"].append("actionTakenForCOVID")
# questions["COVID19Survey"].append("COVIDCaseConfirmed")
# questions["COVID19Survey"].append("numberOfCOVIDCasesConfirmed")
# questions["COVID19Survey"].append("companyPaysForTreatment")
# questions["COVID19Survey"].append("contactTracing")
# questions["COVID19Survey"].append("quarantineProcessForContacted")
# questions["COVID19Survey"].append("sickSalary")
# questions["COVID19Survey"].append("sickHealthMonitoring")
# questions["COVID19Survey"].append("healthInsurance")
# questions["COVID19Survey"].append("hazardPay")
# questions["COVID19Survey"].append("admissionOfVulnerable")
# questions["COVID19Survey"].append("OSHCommittee")
# questions["COVID19Survey"].append("DOLEInspection")

# insert forms into the db
for fn in formnames:
    print(fn)
    insertForm(fn, questions[fn])

for formname in generalComplaintForms:
    addQuestionsToForm(formname, ["companyName"])
    addQuestionsToForm(formname, ["unionPresence"])
    addQuestionsToForm(formname, ["unionHeadContactNo"])
    addQuestionsToForm(formname, ["unionHeadEmail"])
    addQuestionsToForm(formname, ["contactNumber"])
    addQuestionsToForm(formname, ["complaint"])

# addQuestionsToForm("COVID19Survey", questions["COVID19Survey"])

masterAdmin = Administrator(username = 'IOHSAD', email = 'testemail')
masterAdmin.set_password('iohsad2022')
db.session.add(masterAdmin)
commit()

adm = aliased(Administrator, name='adm')
masterAdmin = db.session.query(adm).where(or_(adm.username.like("IOHSAD"), adm.email.like('testemail'))).first()
masterAdmin.email = '2newemail'
commit()
