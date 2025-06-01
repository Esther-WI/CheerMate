from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    gender = Column(String)
    email = Column(String)


class Mood(Base):
    __tablename__ = 'moods'

    id = Column(Integer, primary_key=True)
    feeling = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))

    
class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    mood_trigger = Column(String)
    suggestion = Column(String)
    user_id =  Column(Integer, ForeignKey('users.id'))


