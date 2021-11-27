#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 02:11:42 2021
many to many example in SQLAlchemy
@author: simonque
"""

from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
engine = create_engine('sqlite:///mycollege.db', echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.orm import relationship

class Department(Base):
   __tablename__ = 'department'
   id = Column(Integer, primary_key = True)
   name = Column(String)
   employees = relationship('Employee', secondary = 'link')
   
class Employee(Base):
   __tablename__ = 'employee'
   id = Column(Integer, primary_key = True)
   name = Column(String)
   departments = relationship(Department,secondary='link')
   
class Link(Base):
   __tablename__ = 'link'
   department_id = Column(Integer, ForeignKey('department.id'), primary_key = True)
   employee_id = Column(Integer, ForeignKey('employee.id'), primary_key = True)

Base.metadata.create_all(engine)

d1 = Department(name = "Accounts")
# d2 = Department(name = "Sales")
# d3 = Department(name = "Marketing")

# e1 = Employee(name = "John")
# e2 = Employee(name = "Tony")
# e3 = Employee(name = "Graham")