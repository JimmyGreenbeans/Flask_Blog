"""
Create a file to set up and configure the database
"""

import sys
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

# at the bottom of the file: create an instance of our create engine class which points to the database
engine = create_engine('sqlite:///site.db')

# add Base.metadata.create_all(engine).It will add the classes as new tables in the database we just created
Base.metadata.create_all(engine)