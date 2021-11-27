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
    question_string = Column(String)
    
    form = relationship("Form", back_populates="questions")
    answers = relationship("Answer", back_populates="question")
    
    def __repr__(self):
        return f"Question(id={self.id!r}, form_id={self.form_id!r}, \
            short_name={self.short_name!r}, question_string={self.question_string!r})"

# submissions table class
class Submission(Base):
    __tablename__ = 'Submission'
    id = Column(Integer, primary_key = True)
    date = Column(Date)
    user_id = Column(ForeignKey("User.id"))
    form_type = Column(ForeignKey('Form.id'))
    
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
forms = []
forms.append(Form(form_name = "Form A"))
forms.append(Form(form_name = "Form B"))
for form in forms:
    session.add(form)
    commit()
print()
query(f)

# insert questions
query(q)
questions = []

query(q)

# insert 


engine.dispose()