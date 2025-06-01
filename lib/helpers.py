from lib.db.models import User, Mood , Activity, session
from datetime import datetime
import random

def welcome_user():
    print("Welcome to CheerMate! Let's get started with your mood tracking journey.")
    username = input("Please enter your username: ")    
    user = session.query(User).filter_by(username=username).first()

    if not user:
        print("New user! We'll create a profile for you.")
        gender = input("Enter your gender (Male/Female):")
        email = input("Enter your email: ")
        user = User(username=username, gender=gender, email=email)
        session.add(user)
        session.commit()
        print("User created sucessfully!")
    else:
        print(f"Welcome back, {user.username}!")

    return user


def log_mood(user):
    feeling = input("How are you feeling today? (Happy/Sad/Anxious/Motivated/Frustrated): ")
    mood = Mood(feeling=feeling, user_id=user.id)
    session.add(mood)
    session.commit()
    print("Mood logged successfully!")


def suggest_activity(user):
    activity = random.choice(session.query(Activity).all())
    print(f"\n* Suggested activity for you: {activity.suggestion} (Mood Trigger: {activity.mood_trigger})")


def show_mood_history(user):
    moods = session.query(Mood).filter_by(user_id=user.id).all()
    if moods:
        print("\nYour Mood History:")
        for mood in moods:
            print(f"- {mood.feeling} on {mood.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("No mood history found.")
    
    

def menu():
    print("""
What would you like to do?
1. Log my mood
2. Get activity suggestion
3. View my mood history
4. Exit
""")
    return input("Enter your choice (1-4): ")