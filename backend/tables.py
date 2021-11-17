# Author: Harshvardhan Singh (harshvardhans3@kpmg.com)
# Used for table description

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, LargeBinary, TIMESTAMP
import datetime
from urllib.parse import quote

engine = create_engine('mysql+mysqlconnector://root:%s@localhost:3306/Mindbyte' % quote('pass@word1'))
# engine=create_engine('mysql+mysqlconnector://root:pass@word1@localhost:3306/Mindbyte')
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    password = Column(String(255))


class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    startDate = Column(DateTime)
    endDate = Column(DateTime)
    status = Column(String(255))  # status: ongoing, past, future


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    role = Column(String(255))
    designation = Column(String(255))
    skill = Column(String(255))
    project = Column(Integer, ForeignKey('project.id'))

