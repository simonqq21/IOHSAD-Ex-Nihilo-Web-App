#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 01:55:48 2021

@author: simonque
"""

# -*- coding: utf-8 -*-
"""

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
from datetime import datetime, time, timedelta 
import psycopg2

# initialize psycopg2 engine to connect to postgresql db
engine = create_engine("postgresql+psycopg2://simonque:12345678@localhost/testdb", isolation_level="SERIALIZABLE")
session = Session(engine)
Base = declarative_base() 

# films table
class Film(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    year = Column(Integer, nullable=False)
    actors = relationship("Actor", secondary='actorfilms')
    
    def __repr__(self):
        return f"Film(id={self.id!r}, title={self.title!r}, year={self.year!r})"

# actors table
class Actor(Base):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False, unique=True)
    lastname = Column(String, nullable=False, unique=True)
    birthyear = Column(Integer, nullable=False)
    films = relationship("Film", secondary='actorfilms')
    
    def __repr__(self):
        return f"Actor(id={self.id!r}, lastname={self.lastname!r}, firstname={self.firstname!r}, birthyear={self.birthyear!r})"

# associative table for many-to-many relationship between films and actors
class ActorFilm(Base):
    __tablename__ = 'actorfilms'
    actor_id = Column(ForeignKey('actors.id'), primary_key=True)
    film_id = Column(ForeignKey('films.id'), primary_key=True)
    # actor = relationship(Actor, backref=backref("film_assoc"))
    # film = relationship(Film, backref=backref("actor_assoc"))

Base.metadata.create_all(engine)


engine.dispose()