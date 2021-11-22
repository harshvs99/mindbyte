# Author: Harshvardhan Singh (harshvardhans3@kpmg.com)
# Used for table description

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date
import datetime
from urllib.parse import quote

engine = create_engine('mysql+mysqlconnector://root:%s@localhost:3306/Mindbyte' % quote('pass@word1'))
# engine=create_engine('mysql+mysqlconnector://root:pass@word1@localhost:3306/Mindbyte')
Base = declarative_base()
try:
    Session = sessionmaker()
    Session.configure(bind=engine)
except: 
    Session.rollback()

meta = MetaData()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    password = Column(String(255))


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    employee_name = Column(String(255))
    employee_role = Column(String(255))
    designation = Column(String(255))
    project = Column(Integer, ForeignKey('projects.id'))
    skill = Column(Integer, ForeignKey('skills.id'))


class Skills(Base):
    __tablename__= 'skills'
    id = Column(Integer, primary_key=True)
    skill = Column(String(255))
    # employees = relationship("Employee", back_populates="skill")

    
class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    clientname = Column(String(255))
    projectname = Column(String(255))
    startDate = Column(Date)
    endDate = Column(Date)
    skillsrequired = Column(String(255))
    # employee = relationship("Employee")


class Training(Base):
    __tablename__ = "training"
    id = Column(Integer, primary_key=True)
    trainingname = Column(String(255))
    startDate = Column(Date)
    dueDate = Column(Date)
