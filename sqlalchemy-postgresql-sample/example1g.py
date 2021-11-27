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
    firstname = Column(String, nullable=False, unique=True)
    lastname = Column(String, nullable=False, unique=True)
    birthyear = Column(Integer, nullable=False)
    films = relationship("Film", secondary='actorfilm', overlaps="actors")
    
    def __repr__(self):
        return f"Actor(id={self.id!r}, lastname={self.lastname!r}, firstname={self.firstname!r}, birthyear={self.birthyear!r})"

# associative table for many-to-many relationship between Film and Actor
class ActorFilm(Base):
    __tablename__ = 'actorfilm'
    actor_id = Column(ForeignKey('Actor.id'), primary_key=True)
    film_id = Column(ForeignKey('Film.id'), primary_key=True)

# Base.metadata.create_all(engine)

# code to drop all tables, for testing only
try:
    engine.execute("DROP TABLE simonque.Film CASCADE")
except Exception as err:
    print(err)
    pass
# try:
#     engine.execute("DROP TABLE Actor CASCADE")
# except Exception:
#     pass
# try:
#     engine.execute("DROP TABLE actorfilm CASCADE")
# except Exception:
#     pass

def commit():
    try:
        session.commit()
    except Exception as err:
        print(type(err))
        # print(err)
        session.rollback()
    
# insert films and actors and commit
film1 = Film(title="Spider Man", year=2002)
film2 = Film(title="Iron Man", year=2008)
actor1 = Actor(firstname="Tobey", lastname="Maguire", birthyear=1982)
actor2 = Actor(firstname="Kirsten", lastname="Dunst", birthyear=1985)
actor3 = Actor(firstname="Willem", lastname="Dafoe", birthyear=1979)
actor4 = Actor(firstname="Robert", lastname="Downey", birthyear=1975)
actor5 = Actor(firstname="Gwyneth", lastname="Paltrow", birthyear=1981)
actor6 = Actor(firstname="Terrence", lastname="Howard", birthyear=1986)
session.add(film1)
session.add(film2)
session.add(actor1)
session.add(actor2)
session.add(actor3)
session.add(actor4)
session.add(actor5)
session.add(actor6)
commit()

# define tablename aliases
a = aliased(Actor, name='a')
f = aliased(Film, name='f')

# select the film "Spider Man"
film1 = session.query(f).filter(f.title == "Spider Man").first()
# select the actor with id 1
actor1 = session.query(a).filter(and_(a.firstname == "Tobey"), (a.lastname == "Maguire")).first()

# display the ids of the selected actor and film
print("\nIDs of first film and first actor inserted")
print(actor1.id)
print(film1.id)
# create an entry in the association table relating film1 and actor1
a1f1 = ActorFilm(actor_id=actor1.id, film_id=film1.id)
# add the entry and commit 
session.add(a1f1)
commit()

# select all films and place them in arrays
actors = []
for instance in session.query(a):
    actors.append(instance)
print("All actors in db:")
print(actors)
# select all films and place them in arrays
films = []
for instance in session.query(f):
    films.append(instance)
print("All films in db:")
print(films)

# create relationships between films and actors
print("\nCreate relationships between films and actors")
AFRelationships = []
for i in range(len(films)):
    for j in range(4):
        # print(f"{films[i].id}, {actors[j+2*i].id}")
        AFRelationships.append(ActorFilm(actor_id=actors[j+2*i].id, film_id=films[i].id))
        
print()
print("\nCommit relationships between films and actors")
for af in AFRelationships:
    session.add(af)
    commit()
 
# select all actors per film
print()
af = aliased(ActorFilm, name='af')
for film in films:
    print(f"Actors in the film {film.title}")
    inner_stmt = session.query(af).filter(af.film_id == film.id).subquery()
    # stmt = session.query(a).innerjoin(inner_stmt, a.id==inner_stmt.film_id)
    for instance in session.query(a).join(inner_stmt, a.id==inner_stmt.c.actor_id).order_by(desc(a.lastname)).all():
        print(instance)
    print()
    
# delete
print("delete all films")
for film in films:
    session.delete(film)
    commit()
print("delete all actors")
for actor in actors:
    session.delete(actor)
    commit()
    
# select all films and place them in arrays
print("no more films and actors")
actors = []
for instance in session.query(a):
    actors.append(instance)
print(actors)
# select all films and place them in arrays
films = []
for instance in session.query(f):
    films.append(instance)
print(films)
actorfilms = []
for instance in session.query(af):
    films.append(instance)
print(actorfilms)

engine.dispose()