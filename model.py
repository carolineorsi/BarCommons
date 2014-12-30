from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Float, String, Boolean, Text, and_, or_
from sqlalchemy.orm import sessionmaker, relationship, backref
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session
from sqlalchemy import ForeignKey
from app import app
import os

db = SQLAlchemy(app)

DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://dafjsxehbywvux:hmaDRyyu8As6uTU9t1lCahEm5X@ec2-54-204-45-196.compute-1.amazonaws.com:5432/d4qboj00bqn958")
engine = create_engine(DATABASE_URL, echo=False)
session = scoped_session(sessionmaker(bind=engine,
                                      autocommit=False,
                                      autoflush=False))

Base = declarative_base()
Base.query = session.query_property()


class Rule(db.Model):
    __tablename__ = "rule"

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    description = Column(Text)
    source = Column(String(64))
    subject_id = Column(Integer, ForeignKey('subject.id'))
    knowledge_level = Column(String(64))

    subject = relationship("Subject", backref=backref("rule", order_by=id))


class Subject(db.Model):
    __tablename__ = "subject"

    id = Column(Integer, primary_key=True)
    title = Column(String(64))
    parent = Column(Integer)
    lft = Column(Integer, nullable=False)
    rght = Column(Integer, nullable=False)


class Question(db.Model):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    rule_id = Column(Integer, ForeignKey('rule.id'))
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    ranking = Column(Integer)
    question_type = Column(String(64))

    rule = relationship("Rule", backref=backref("question", order_by=id))

# class Waypoint(db.Model):
#     __tablename__ = "waypoints"

#     id = Column(Integer, primary_key=True)
#     name = Column(String(120), nullable=False)
#     address = Column(String(250))
#     route_id = Column(Integer, ForeignKey('routes.id'))
#     user_id = Column(Integer, ForeignKey('users.id'))
#     lat = Column(Float, nullable=False)
#     lng = Column(Float, nullable=False)
#     google_id = Column(String(60))
#     stopnum = Column(Integer)
#     stopover = Column(Boolean)

#     route = relationship("Route", backref=backref("waypoints", order_by=id))
#     user = relationship("User", backref=backref("waypoints", order_by=id))


def connect():
    """ Used for connecting and creating the database. """

    global ENGINE
    global Session

    ENGINE = create_engine(DATABASE_URL, echo=False)
    Session = sessionmaker(bind=ENGINE)
    return Session()


def main():
    pass


if __name__ == "__main__":
    main()