from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime
from sqlalchemy import create_engine

engine= create_engine('sqlite:////home/user/Desktop/Phase_3-Project/CheerMate/lib/db/cheermate.db')
Session= sessionmaker(bind=engine)
session= Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    email = Column(String, nullable=False)

    moods = relationship("Mood", backref="user", cascade="all, delete" )
    activities = relationship("Activity", backref="user", cascade="all, delete")

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"
    
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not value.strip():
            raise ValueError("Username cannot be empty.")
        self._username = value.strip()
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError("Invalid email address")
        self._email = value


    @classmethod
    def create(cls, username, gender, email):
        user=cls(username=username, gender=gender, email=email)
        session.add(user)
        session.commit()
        return user
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).get(cls, id)
    
    def delete(self):
        session.delete(self)
        session.commit()
        


class Mood(Base):
    __tablename__ = 'moods'

    id = Column(Integer, primary_key=True)
    feeling = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f"<Mood(feeling='{self.feeling}', timestamp='{self.timestamp}')>"

    @property
    def feeling(self):
        return self._feeling

    @feeling.setter
    def feeling(self, value):
        if not value.strip():
            raise ValueError("Mood feeling cannot be empty.")
        self._feeling = value.strip()

    @classmethod
    def create(cls, feeling, user_id):
        mood = cls(feeling=feeling, user_id=user_id)
        session.add(mood)
        session.commit()
        return mood
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).get(cls, id)
    
    def delete(self):
        session.delete(self)
        session.commit()

    
class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    mood_trigger = Column(String, nullable=False)
    suggestion = Column(String, nullable=False)
    user_id =  Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f"<Activity(mood_trigger='{self.mood_trigger}', suggestion='{self.suggestion}')>"
    
    @property
    def mood_trigger(self):
        return self._mood_trigger

    @mood_trigger.setter
    def mood_trigger(self, value):
        if not value.strip():
            raise ValueError("Mood trigger cannot be empty.")
        self._mood_trigger = value.strip()

    @classmethod
    def create(cls, mood_trigger, suggestion, user_id ):
        activity= cls(mood_trigger=mood_trigger, suggestion=suggestion, user_id=user_id)
        session.add(activity)
        session.commit()
        return activity
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).get(cls, id)
    
    def delete(self):
        session.delete(self)
        session.commit()


    
