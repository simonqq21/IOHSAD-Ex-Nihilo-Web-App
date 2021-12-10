#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 20:02:57 2021

@author: simonque
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, relationship, backref
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from sqlalchemy import select, insert, update, delete
from sqlalchemy import func, cast
from sqlalchemy.orm import Bundle, aliased
from sqlalchemy import and_, or_
from sqlalchemy.pool import StaticPool
from sqlalchemy import UniqueConstraint
from sqlalchemy import asc, desc
from datetime import datetime, date, time, timedelta
import psycopg2

def commit():
    try:
        session.commit()
    except Exception as err:
        print(type(err))
        # print(err)
        session.rollback()
        session.close()

# initialize psycopg2 engine to connect to postgresql db
engine = create_engine("postgresql+psycopg2://simonque:12345678@localhost/swengdb", \
                       isolation_level="SERIALIZABLE")
session = Session(engine, autoflush=False)
Base = declarative_base()

# forms table class
class Form(Base):
    __tablename__ = 'Form'
    id = Column(Integer, primary_key=True)
    form_name = Column(String, unique=True)

    questions = relationship("Question", back_populates="form", cascade="all, delete, delete-orphan")
    submissions = relationship("Submission", back_populates="form", cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"Form(id={self.id!r}, form_name={self.form_name!r})"

# questions table class
class Question(Base):
    __tablename__ = 'Question'
    id = Column(Integer, primary_key = True)
    form_id = Column(ForeignKey('Form.id'))
    short_name = Column(String)

    form_question = UniqueConstraint(form_id, short_name, name="form_question")
    form = relationship("Form", back_populates="questions")
    answers = relationship("Answer", back_populates="question", cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"Question(id={self.id!r}, form_id={self.form_id!r}, short_name={self.short_name!r})"

# submissions table class
class Submission(Base):
    __tablename__ = 'Submission'
    id = Column(Integer, primary_key = True)
    date = Column(Date, nullable=False)
    user_id = Column(ForeignKey("User.id"))
    form_type = Column(ForeignKey('Form.id'), nullable=False)

    user_form = UniqueConstraint(user_id, form_type, name="user_form")
    form = relationship("Form", back_populates="submissions")
    user = relationship("User", back_populates="submissions")
    answers = relationship("Answer", back_populates="submission", cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"Submission(id={self.id!r}, date={self.date!r}, user_id={self.user_id!r}, \
            form_type={self.form_type!r})"

# users table class
class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key = True)
    username = Column(String, unique=True)

    submissions = relationship("Submission", back_populates="user", cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id!r}, username={self.username!r})"

# answers table class
class Answer(Base):
    __tablename__ = 'Answer'
    id = Column(Integer, primary_key=True)
    submission_id = Column(ForeignKey("Submission.id"))
    question_id = Column(ForeignKey('Question.id'))
    answer_string = Column(String)

    submission = relationship("Submission", back_populates="answers")
    question = relationship("Question", back_populates="answers")

    def __repr__(self):
        return f"Answer(submission_id={self.submission_id!r}, question_id={self.question_id!r}, \
            answer_string={self.answer_string!r})"

# define table aliases
f = aliased(Form, name='f')
q = aliased(Question, name='q')
s = aliased(Submission, name='s')
u = aliased(User, name='u')
a = aliased(Answer, name='a')

# uncomment to drop all tables, for testing only
# try:
#     engine.execute('''DROP TABLE "User" CASCADE''')
# except Exception as err:
#     print(err)
#     pass
# try:
#     engine.execute('DROP TABLE "Question" CASCADE')
# except Exception as err:
#     print(err)
#     pass
# try:
#     engine.execute('DROP TABLE "Submission" CASCADE')
# except Exception as err:
#     print(err)
#     pass
# try:
#     engine.execute('DROP TABLE "Form" CASCADE')
# except Exception as err:
#     print(err)
#     pass
# try:
#     engine.execute('DROP TABLE "Answer" CASCADE')
# except Exception as err:
#     print(err)
#     pass
Base.metadata.create_all(engine)

def query(alias):
    items = []
    for instance in session.query(alias):
        items.append(instance)
    print(items)

'''
method to insert new form with a set of questions
If the form exists
form_name (string) - form name
questions (list of strings) - the list of short question names
'''
def insertForm(formName, questions):
    global session
    newForm = Form(form_name=formName)
    session.add(newForm)
    commit()
    for question in questions:
        newForm.questions.append(Question(short_name=question))
        commit()

'''
method to select all forms that currently exist in the database.
'''
def selectAllFormNames():
    global session, f
    formnames = []
    for instance in session.query(f):
        formnames.append(instance)
    return formnames

'''
method to select a single form given a keyword string
Questions can be accessed from the form using the questions attribute of the form.
formNameLike (string) - form name search string wildcard
'''
def selectForm(formNameLike):
    global session, f
    form = session.query(f).where(f.form_name.like(f"%{formNameLike}%")).first()
    return form

'''
method to rename a form
oldFormName (string)
newFormName (string)
'''
def renameForm(oldFormName, newFormName):
    global session, f
    form = session.query(f).where(f.form_name.like(f"{oldFormName}")).first()
    if form is not None:
        form.form_name = newFormName
        commit()

'''
method to add a question to a form that exists
formName (string) - exact name of form
questionShortNames (list of string) - list of question short names
'''
def addQuestionsToForm(formName, questionShortNames):
    global session, f, q
    form = session.query(f).where(f.form_name.like(formName)).first()
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
    global session, q
    fId = session.query(f.id).where(f.form_name.like(formName)).first()[0]
    print(fId)
    for name in questionShortNames:
        question = session.query(q).where(and_(q.short_name.like(name), q.form_id == fId)).first()
        if question is not None:
            session.delete(question)
            commit()

'''
method to delete a form together with all its questions
'''
def deleteForm(formName):
    global session, f
    form = session.query(f).where(f.form_name.like(f"{formName}")).first()
    if form is not None:
        session.delete(form)
        commit()

'''
method to insert a form submission together with the user and all answers
date (date) - date submitted
username (string) - unique username
formname (string) - form name
questionsAndAnswers (list of tuples) - list of tuples containing the question short name and answer
'''
def submitForm(submitDate, username, formName, questionsAndAnswers):
    global session, a, f, q, s, u

    submission = Submission()
    submission.date = submitDate
    user = session.query(u).where(u.username.like(username)).first()
    print(user)
    if user is None:
        user = User(username=username)
        session.add(user)
        commit()
    submission.user = user

    form = session.query(f).where(f.form_name.like(formName)).first()
    print(form)
    if form is not None:
        submission.form = form

        for qa in questionsAndAnswers:
            # question = session.query(q).where(and_(q.short_name.like(qa[0]), q.form_id == form.id)).first()
            question = session.query(q).where(q.short_name.like(qa[0])).first()
            if question is not None:
                print(question)
                answer = Answer(answer_string = qa[1], question=question)
                submission.answers.append(answer)

    session.add(submission)
    commit()

'''

'''


# insert forms A and B
formnames = []
formnames.append("Form A")
formnames.append("Form B")

# insert questions
questions = {}
# questions for Form A
questions["Form A"] = []
questions["Form A"].append("name")
questions["Form A"].append("age")
questions["Form A"].append("sex")
questions["Form A"].append("civilStatus")
questions["Form A"].append( "education")
questions["Form A"].append("position")
questions["Form A"].append("yearsWorked")
questions["Form A"].append("workStatus")
questions["Form A"].append("wage")
questions["Form A"].append("benefits")
questions["Form A"].append("benefitsReceived")
questions["Form A"].append("hoursPerDay")
questions["Form A"].append("chemicalUse")
questions["Form A"].append("chemicalName")
questions["Form A"].append("chemicalPurpose")
questions["Form A"].append("chemExposureDuration")
questions["Form A"].append("diseaseAccidented")
questions["Form A"].append("treatmentBillSource")
questions["Form A"].append("treatmentLocation")
questions["Form A"].append("reproductiveProblem")
questions["Form A"].append("knowOthersSickAccidented")
questions["Form A"].append("yearlyPhysicalExamination")
questions["Form A"].append("workPPE")
questions["Form A"].append("workPPEFree")
questions["Form A"].append("workHazards")
questions["Form A"].append("wasteDisposal")
questions["Form A"].append("DOLEInspection")
questions["Form A"].append("safetyOfficerPresent")

# questions for Form B
questions["Form B"] = []
questions["Form B"].append("name")
questions["Form B"].append("address")
questions["Form B"].append("age")
questions["Form B"].append("sex")
questions["Form B"].append("civilStatus")
questions["Form B"].append("occupation")
questions["Form B"].append("employingCompanyName")
questions["Form B"].append("chiefComplaint")
questions["Form B"].append("presentMedicalHistory")
questions["Form B"].append("pastMedicalHistory")
questions["Form B"].append("pastPersonalHistory")
questions["Form B"].append("familyMedicalHistory")
questions["Form B"].append("pastJob")
questions["Form B"].append("pastJobDuration")
questions["Form B"].append("currentJob")
questions["Form B"].append("currentJobSection")
questions["Form B"].append("currentJobDuration")
questions["Form B"].append("currentJobDescription")
questions["Form B"].append("currentJobHazards")
questions["Form B"].append("medicalHistorySHEENT")
questions["Form B"].append("medicalHistoryRespiratory")
questions["Form B"].append("medicalHistoryCirculatory")
questions["Form B"].append("medicalHistoryDigestive")
questions["Form B"].append("medicalHistoryUrogenital")
questions["Form B"].append("medicalHistoryEndocrine")
questions["Form B"].append("medicalHistoryNervous")
questions["Form B"].append("medicalHistoryMusculoskeletal")
questions["Form B"].append("vitalSignBP")
questions["Form B"].append("vitalSignPR")
questions["Form B"].append("vitalSignTemp")
questions["Form B"].append("vitalSignWeight")
questions["Form B"].append("generalAppearance")
questions["Form B"].append("physicalExaminationSHEENT")
questions["Form B"].append("physicalExaminationLungs")
questions["Form B"].append("physicalExaminationHeart")
questions["Form B"].append("physicalExaminationAbdomen")
questions["Form B"].append("physicalExaminationExtremities")
questions["Form B"].append("diagnosis")
questions["Form B"].append("management")
# insert forms A and B into the db
for fn in formnames:
    insertForm(fn, questions[fn])

# extra questions
addQuestionsToForm("Form A", ["companyName"])
addQuestionsToForm("Form A", ["unionPresence"])
addQuestionsToForm("Form A", ["unionHeadContactNo"])
addQuestionsToForm("Form A", ["unionHeadEmail"])
addQuestionsToForm("Form A", ["contactNumber"])
addQuestionsToForm("Form A", ["complaint"])

print()
# query(q)
print()
# testing code
insertForm("Form C", [])
# insertForm("Form C", ["qA", "qB", 'qC'])
# print()
# print(selectAllFormNames())
# print()
# print(selectForm("C"))
# print()
# renameForm("Form C", "Form Z")
# print(selectAllFormNames())
# addQuestionsToForm("Form Z", ["qZ"])
# print(selectForm("Form Z").questions)
# deleteForm("Form C")
addQuestionsToForm("Form C", ["qA", "qB"])
addQuestionsToForm("Form C", ["qC"])
# print(selectForm("C").questions)
# deleteQuestions("Form C", ["qA","qB"])
# print(selectForm("C").questions)

# submitForm(date.today(), "tuser", "Form C", [("qC", "aC"), ("qB", "aB"), ("qA", "aA")])
# submitForm(date.today(), "tuser2", "Form C", [("qC", "aC2"), ("qB", "aB2"), ("qA", "aA2")])
# submitForm(date.today(), "tuser", "Form A", [("name", "Test1"), ("age", "232")])
# submitForm(date.today(), "tuser3", "Form C", [("qB", "aB2"), ("qA", "aA2")])



engine.dispose()
