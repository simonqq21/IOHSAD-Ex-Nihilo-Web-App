#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 23:44:06 2021
many-to-many example in SQLAlchemy
@author: simonque
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, relationship
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime, Text
from sqlalchemy import select, insert, update, delete
from sqlalchemy import func, cast
from sqlalchemy.orm import Bundle, aliased 
from sqlalchemy import and_, or_
from sqlalchemy.pool import StaticPool 
from sqlalchemy import UniqueConstraint
from datetime import datetime, time, timedelta 
import psycopg2

engine = create_engine("postgresql+psycopg2://simonque:12345678@localhost/testdb", isolation_level="SERIALIZABLE")
session = Session(engine)
Base = declarative_base() 

association_table = Table('association', Base.metadata,
    Column('left_id', ForeignKey('left.id'), primary_key=True),
    Column('right_id', ForeignKey('right.id'), primary_key=True)
)

class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    children = relationship(
        "Child",
        secondary=association_table,
        back_populates="parents")

class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    parents = relationship(
        "Parent",
        secondary=association_table,
        back_populates="children")
    
Base.metadata.create_all(engine)

parent1 = Parent(value=1)
child1 = Child(value=2)
parent1.children.append(child1)
session.add(parent1)
session.add(child1)
session.commit()

child2 = Child(value=3)
parent1.children.append(child2)
session.add(child2)
session.add(parent1)
session.commit()
