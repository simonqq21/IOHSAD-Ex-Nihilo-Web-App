# -*- coding: utf-8 -*-
"""
many to many example in SQLAlchemy
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

# initialize psycopg2 engine to connect to postgresql db
engine = create_engine("postgresql+psycopg2://simonque:12345678@localhost/testdb", isolation_level="SERIALIZABLE")
session = Session(engine)
Base = declarative_base() 

def commit():
    try:
        session.commit()
    except Exception as err:
        print(type(err))
        # print(err)
        session.rollback()
        
# Film table
class Film(Base):
    __tablename__ = 'Film'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    year = Column(Integer, nullable=False)
    actors = relationship("Actor", secondary='actorfilm')
    
    def __repr__(self):
        return f"Film(id={self.id!r}, title={self.title!r}, year={self.year!r})"

# Actor table
class Actor(Base):
    __tablename__ = 'Actor'
    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    birthyear = Column(Integer, nullable=False)
    firstlastname = UniqueConstraint(firstname, lastname, name='firstlastname')
    films = relationship("Film", secondary='actorfilm', overlaps="actors")
    
    def __repr__(self):
        return f"Actor(id={self.id!r}, lastname={self.lastname!r}, firstname={self.firstname!r}, birthyear={self.birthyear!r})"

# associative table for many-to-many relationship between Film and Actor
class ActorFilm(Base):
    __tablename__ = 'actorfilm'
    actor_id = Column(ForeignKey('Actor.id'), primary_key=True)
    film_id = Column(ForeignKey('Film.id'), primary_key=True)

Base.metadata.create_all(engine)

# code to drop all tables, for testing only
# try:
#     engine.execute('DROP TABLE "Film" CASCADE')
# except Exception as err:
#     print(err)
#     pass
# try:
#     engine.execute('DROP TABLE "Actor" CASCADE')
# except Exception as err:
#     print(err)
#     pass
# try:
#     engine.execute('DROP TABLE "actorfilm" CASCADE')
# except Exception as err:
#     print(err)
#     pass

actor1 = Actor(firstname="a", lastname="b", birthyear=2000)
session.add(actor1)
commit()
actor2 = Actor(firstname="a", lastname="b", birthyear=2001)
session.add(actor2)
commit()
actor3 = Actor(firstname="a", lastname="c", birthyear=2002)
session.add(actor3)
commit()