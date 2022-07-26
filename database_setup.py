"""
Create a file to set up and configure the database
"""

import sys
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# for creating the mapper code, we import Column, ForeignKey, Integer, and String to define our database table columns.
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
db = SQLAlchemy(app)

#for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

#for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship

#for configuration
from sqlalchemy import create_engine

#create declarative_base instance from which all mapped classes should inherit.
Base = declarative_base()

#Connect to Database and create database session
engine = create_engine('sqlite:///site.db')
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.
session = DBSession()

#Classes
# DB classes - called Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=True, default='default.jpg')
    password = db.Column(db.String(60), nullable=True)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

# at the bottom of the file: create an instance of our create engine class which points to the database
engine = create_engine('sqlite:///site.db')

# add Base.metadata.create_all(engine).It will add the classes as new tables in the database we just created
Base.metadata.create_all(engine)