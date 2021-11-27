#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:54:31 2021
one-to-many example in SQLAlchemy
@author: simonque
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, relationship
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Date, DateTime
from sqlalchemy import select, insert, update, delete
from sqlalchemy import func, cast
from sqlalchemy.orm import Bundle, aliased 
from sqlalchemy import and_, or_
from sqlalchemy.pool import StaticPool 
from sqlalchemy import UniqueConstraint
from datetime import datetime, time, timedelta 
import psycopg2

# initialize psycopg2 engine to connect to postgresql db
engine = create_engine("postgresql+psycopg2://simonque:12345678@localhost/testdb1", isolation_level="SERIALIZABLE")
session = Session(engine)
Base = declarative_base() 

class User(Base):
    __tablename__ = 'user_account'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    fullname = Column(String, unique=True, nullable=False)
    addresses = relationship("Address", back_populates="user")
    
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
    
class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user_account.id"))
    email_address = Column(String, unique=True, nullable=False)
    user = relationship("User", back_populates="addresses")
    
    def __repr__(self):
        return f"Addresses(id={self.id!r}, user_id={self.user_id!r}, email_address={self.email_address!r})"

# try:
#     engine.execute("DROP TABLE user_account CASCADE")
# except Exception:
#     pass
# try:
#     engine.execute("DROP TABLE Address CASCADE")
# except Exception:
#     pass
Base.metadata.create_all(engine)


u1 = User(name='pkrabs', fullname='Pearl Krabs')
# print(type(u1))
a1 = Address(email_address="pearl.krabs@gmail.com")
a2 = Address(email_address="pearl@aol.com", user=u1)
a3 = Address(email_address="pearl123@yahoo.com")

print(u1.addresses)

u1.addresses.append(a1)
print(u1.addresses)
print(a1.user)

session.add(u1)

# print(u1 in session)
# print(a1 in session)
# print(a2 in session)

# print(u1.id)
# print(a1.user_id)

try:
    session.commit()
except Exception as err:
    print(type(err))
    session.rollback()

print()
u = aliased(User, name='u')
stmt = select(u).where(u.name.like("%krabs%"))
for row in session.execute(stmt):
    print(type(row))
    u1 = row[0]
    
print(u1)
u1.addresses.append(a3)
print(u1 in session.dirty)
try:
    session.commit()
except Exception as err:
    print(type(err))
    session.rollback()
print(u1 in session.dirty)
# print(u1.id)

engine.dispose()
