from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime
 

engine= create_engine('sqlite:////home/user/Desktop/Phase_3-Project/CheerMate/lib/db/cheermate.db')
Session= sessionmaker(bind=engine)
session= Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    _username = Column("username", String, nullable=False)
    gender = Column(String, nullable=False)
    _email = Column("email", String, nullable=False)

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
        if not username.strip():
            raise ValueError("Username cannot be empty.")
        if '@' not in email:
            raise ValueError("Invalid email format.")
        user=cls(username=username, gender=gender, email=email.strip())
        session.add(user)
        session.commit()
        return user
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.get(cls, id)
    
    def delete(self):
        session.delete(self)
        session.commit()
        


class Mood(Base):
    __tablename__ = 'moods'

    id = Column(Integer, primary_key=True)
    _feeling = Column("feeling", String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)

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
        if not feeling.strip():
            raise ValueError("Feeling cannot be empty.")
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer.")
        mood = cls(feeling=feeling, user_id=user_id)
        session.add(mood)
        session.commit()
        return mood
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.get(cls, id)
    
    def delete(self):
        session.delete(self)
        session.commit()

    
class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    _mood_trigger = Column("mood_trigger", String, nullable=False)
    suggestion = Column(String, nullable=False)
    user_id =  Column(Integer, ForeignKey('users.id'), nullable=True)

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
        if not mood_trigger.strip():
            raise ValueError("Mood trigger cannot be empty.")
        if not suggestion.strip():
            raise ValueError("Suggestion cannot be empty.")
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer.")
        activity= cls(mood_trigger=mood_trigger, suggestion=suggestion, user_id=user_id)
        session.add(activity)
        session.commit()
        return activity
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.get(cls, id)
    
    def delete(self):
        session.delete(self)
        session.commit()


    
