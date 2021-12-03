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
from datetime import datetime, time, timedelta 
import psycopg2

def commit():
    try:
        session.commit()
    except Exception as err:
        print(type(err))
        # print(err)
        session.rollback()

# initialize psycopg2 engine to connect to postgresql db
engine = create_engine("postgresql+psycopg2://simonque:12345678@localhost/swengdb", \
                       isolation_level="SERIALIZABLE")
session = Session(engine)
Base = declarative_base() 

# forms table class
class Form(Base):
    __tablename__ = 'Form'
    id = Column(Integer, primary_key=True)
    form_name = Column(String, unique=True)
    
    questions = relationship("Question", back_populates="form")
    submissions = relationship("Submission", back_populates="form")
    
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
    answers = relationship("Answer", back_populates="question")
    
    def __repr__(self):
        return f"Question(id={self.id!r}, form_id={self.form_id!r}, short_name={self.short_name!r})"

# submissions table class
class Submission(Base):
    __tablename__ = 'Submission'
    id = Column(Integer, primary_key = True)
    date = Column(Date)
    user_id = Column(ForeignKey("User.id"))
    form_type = Column(ForeignKey('Form.id'))
    
    user_form = UniqueConstraint(user_id, form_type, name="user_form")
    form = relationship("Form", back_populates="submissions")
    user = relationship("User", back_populates="submissions")
    answers = relationship("Answer", back_populates="submission")
    
    def __repr__(self):
        return f"Submission(id={self.id!r}, date={self.date!r}, user_id={self.user_id!r}, \
            form_type={self.form_type!r})"
    
# users table class
class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key = True)
    username = Column(String, unique=True)
    
    submissions = relationship("Submission", back_populates="user")
    
    def __repr__(self):
        return f"User(id={self.id!r}, username={self.username!r})"
    
# answers table class
class Answer(Base):
    __tablename__ = 'Answer'
    submission_id = Column(ForeignKey("Submission.id"), primary_key = True)
    question_id = Column(ForeignKey('Question.id'), primary_key = True)
    answer_string = Column(String)
    
    submission = relationship("Submission", back_populates="answers")
    question = relationship("Question", back_populates="answers")
    
    def __repr__(self):
        return f"Answer(submission_id={self.submission_id!r}, question_id={self.question_id!r}, \
            answer_string={self.answer_string!r})"
    
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



# define table aliases
f = aliased(Form, name='f')
q = aliased(Question, name='q')
s = aliased(Submission, name='s')
u = aliased(User, name='u')
a = aliased(Answer, name='a')

def query(alias):
    items = []
    for instance in session.query(alias):
        items.append(instance)
    print(items)
    
# insert form types
query(f)
# items = []
# for instance in session.query(f):
#     session.delete(instance)
#     commit()
# print(items)
formsdata = []
formsdata.append(("Form A",))
formsdata.append(("Form B",))
print(formsdata)
for data in formsdata:
    session.add(Form(form_name=data[0]))
    commit()
print()
query(f)

# insert questions
query(q)
questionsdata = []
form_ids = {}
form_ids["Form A"] = session.query(f.id).filter(f.form_name=="Form A").first()[0]
form_ids["Form B"] = session.query(f.id).filter(f.form_name=="Form B").first()[0]
# questions for Form A
questionsdata.append((form_ids["Form A"], "name"))
questionsdata.append((form_ids["Form A"], "age"))
questionsdata.append((form_ids["Form A"], "sex"))
questionsdata.append((form_ids["Form A"], "civilStatus"))
questionsdata.append((form_ids["Form A"], "education"))
questionsdata.append((form_ids["Form A"], "position"))
questionsdata.append((form_ids["Form A"], "yearsWorked"))
questionsdata.append((form_ids["Form A"], "workStatus"))
questionsdata.append((form_ids["Form A"], "wage"))
questionsdata.append((form_ids["Form A"], "benefits"))
questionsdata.append((form_ids["Form A"], "benefitsReceived"))
questionsdata.append((form_ids["Form A"], "hoursPerDay"))
questionsdata.append((form_ids["Form A"], "chemicalUse"))
questionsdata.append((form_ids["Form A"], "chemicalName"))
questionsdata.append((form_ids["Form A"], "chemicalPurpose"))
questionsdata.append((form_ids["Form A"], "chemExposureDuration"))
questionsdata.append((form_ids["Form A"], "diseaseAccidented"))
questionsdata.append((form_ids["Form A"], "treatmentBillSource"))
questionsdata.append((form_ids["Form A"], "treatmentLocation"))
questionsdata.append((form_ids["Form A"], "reproductiveProblem"))
questionsdata.append((form_ids["Form A"], "knowOthersSickAccidented"))
questionsdata.append((form_ids["Form A"], "yearlyPhysicalExamination"))
questionsdata.append((form_ids["Form A"], "workPPE"))
questionsdata.append((form_ids["Form A"], "workPPEFree"))
questionsdata.append((form_ids["Form A"], "workHazards"))
questionsdata.append((form_ids["Form A"], "wasteDisposal"))
questionsdata.append((form_ids["Form A"], "DOLEInspection"))
questionsdata.append((form_ids["Form A"], "safetyOfficerPresent"))
# questions for Form B
questionsdata.append((form_ids["Form B"], "name"))
questionsdata.append((form_ids["Form B"], "address"))
questionsdata.append((form_ids["Form B"], "age"))
questionsdata.append((form_ids["Form B"], "sex"))
questionsdata.append((form_ids["Form B"], "civilStatus"))
questionsdata.append((form_ids["Form B"], "occupation"))
questionsdata.append((form_ids["Form B"], "employingCompanyName"))
questionsdata.append((form_ids["Form B"], "chiefComplaint"))
questionsdata.append((form_ids["Form B"], "presentMedicalHistory"))
questionsdata.append((form_ids["Form B"], "pastMedicalHistory"))
questionsdata.append((form_ids["Form B"], "pastPersonalHistory"))
questionsdata.append((form_ids["Form B"], "familyMedicalHistory"))
questionsdata.append((form_ids["Form B"], "pastJob"))
questionsdata.append((form_ids["Form B"], "pastJobDuration"))
questionsdata.append((form_ids["Form B"], "currentJob"))
questionsdata.append((form_ids["Form B"], "currentJobSection"))
questionsdata.append((form_ids["Form B"], "currentJobDuration"))
questionsdata.append((form_ids["Form B"], "currentJobDescription"))
questionsdata.append((form_ids["Form B"], "currentJobHazards"))
questionsdata.append((form_ids["Form B"], "medicalHistorySHEENT"))
questionsdata.append((form_ids["Form B"], "medicalHistoryRespiratory"))
questionsdata.append((form_ids["Form B"], "medicalHistoryCirculatory"))
questionsdata.append((form_ids["Form B"], "medicalHistoryDigestive"))
questionsdata.append((form_ids["Form B"], "medicalHistoryUrogenital"))
questionsdata.append((form_ids["Form B"], "medicalHistoryEndocrine"))
questionsdata.append((form_ids["Form B"], "medicalHistoryNervous"))
questionsdata.append((form_ids["Form B"], "medicalHistoryMusculoskeletal"))
questionsdata.append((form_ids["Form B"], "vitalSignBP"))
questionsdata.append((form_ids["Form B"], "vitalSignPR"))
questionsdata.append((form_ids["Form B"], "vitalSignTemp"))
questionsdata.append((form_ids["Form B"], "vitalSignWeight"))
questionsdata.append((form_ids["Form B"], "generalAppearance"))
questionsdata.append((form_ids["Form B"], "physicalExaminationSHEENT"))
questionsdata.append((form_ids["Form B"], "physicalExaminationLungs"))
questionsdata.append((form_ids["Form B"], "physicalExaminationHeart"))
questionsdata.append((form_ids["Form B"], "physicalExaminationAbdomen"))
questionsdata.append((form_ids["Form B"], "physicalExaminationExtremities"))
questionsdata.append((form_ids["Form B"], "diagnosis"))
questionsdata.append((form_ids["Form B"], "management"))
# print(questionsdata)
for data in questionsdata:
    session.add(Question(form_id=data[0], short_name=data[1]))
    commit()
print()
query(q)

'''method to insert new form with a set of questions
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
    print("inserted")

# method to select all form names
def selectAllFormNames():
    pass

# method to select a form with all its questions
def selectForm():
    pass

# method to rename a form
def renameForm():
    pass

# method to add a question to a form that exists
def addQuestionToForm():
    pass


# method to remove a question from a form that exists


# method to delete a form together with all its questions


# method to insert a form submission together with the user and all answers

insertForm("Form C", ["qA", "qB", 'qC'])
insertForm("Form A", ["qA", "qB", 'qC'])

engine.dispose()