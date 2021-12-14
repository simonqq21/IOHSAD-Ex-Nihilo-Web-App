from app import db
from datetime import date
from sqlalchemy.orm import aliased

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
    emailPhone = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True)

    submissions = db.relationship("Submission", back_populates="user", cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id!r}, username={self.username!r})"

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
user (tuple of string) - user represented by tuple (<username>, <emailPhone>)
formname (string) - form name
questionsAndAnswers (list of tuples) - list of tuples containing the question short name and answer
'''
def submitForm(submitDate, user, formName, questionsAndAnswers):
    submission = Submission()
    submission.date = submitDate
    username = user[0]
    emailPhone = user[1]
    user = db.session.query(u).where(u.username.like(username)).first()
    print(user)
    if user is None:
        user = User(username=username, emailPhone=emailPhone)
        db.session.add(user)
        commit()
    submission.user = user
    print("Form")
    form = db.session.query(f).where(f.form_name.like(formName)).first()
    print(f'form={form}')
    if form is not None:
        submission.form = form

        for qa in questionsAndAnswers:
            # question = db.session.query(q).where(and_(q.short_name.like(qa[0]), q.form_id == form.id)).first()
            question = db.session.query(q).where(q.short_name.like(qa[0])).first()
            if question is not None:
                print(question)
                answer = Answer(answer_string = qa[1], question=question)
                submission.answers.append(answer)

        db.session.add(submission)
        commit()
