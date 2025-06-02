from lib.db.models import User, Mood , Activity, session
from datetime import datetime
from sqlalchemy import func
import random


def welcome_user():
    print("Welcome to CheerMate! Let's get started with your mood tracking journey.")

    while True:
        username = input("Please enter your username: ").strip()
        if username:
            break
        print("Username cannot be empty. Please try again.")
    
    user = session.query(User).filter_by(username=username).first()

    if not user:
        print("New user! We'll create a profile for you.")

        while True:
            gender = input("Enter your gender (Male/Female):").strip()
            if gender.lower() in ['male', 'female']:
                break
            print("Please enter 'Male' or 'Female'.")
        while True:
            email = input("Enter your email: ").strip()
            if '@' in email and '.' in email:
                break
            print("Please enter a valid email address.")
        user = User(gender=gender)
        try:
            user.username = username
            user.email = email
            session.add(user)
            session.commit()
            print("User created sucessfully!")
        except ValueError as e:
            print(f"Error creating user: {e}")
            return welcome_user()
    else:
        print(f"Welcome back, {user.username}!")

    return user

 


def log_mood(user):
    valid_feelings = ["Happy", "Sad", "Anxious", "Motivated", "Frustrated"]
    
    while True:
        feeling = input("How are you feeling today? (Happy/Sad/Anxious/Motivated/Frustrated): ").strip()
        if feeling in valid_feelings:
            break
        print("Please enter one of the listed moods.")
    mood = Mood(feeling=feeling.capitalize(), user_id=user.id)
    session.add(mood)
    session.commit()
    print("Mood logged successfully!")


def suggest_activity(user):
    last_mood = session.query(Mood).filter_by(user_id=user.id).order_by(Mood.timestamp.desc()).first()
    if last_mood:
        print(f"DEBUG: Last mood = '{last_mood.feeling}'")
        activities = session.query(Activity).filter(func.lower(Activity._mood_trigger) == last_mood.feeling.lower()).all()
        if activities:
            activity = random.choice(activities)
            print(f"\n* Suggested activity for your mood ({last_mood.feeling}): {activity.suggestion}")
        else:
            print("No activities found for your current mood.")
    else:
        print("Please log a mood first to get suggestions.")


def show_mood_history(user):
    moods = session.query(Mood).filter_by(user_id=user.id).order_by(Mood.timestamp.desc()).all()
    if moods:
        print("\nYour Mood History:")
        for mood in moods:
            print(f"- {mood.feeling} on {mood.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("No mood history found.")
    
def delete_last_mood_entry(user):
    last_mood = session.query(Mood).filter_by(user_id=user.id).order_by(Mood.timestamp.desc()).first()
    if last_mood:
        session.delete(last_mood)
        session.commit()
        print("Last mood entry deleted successfully!")
    else:
        print("No mood entries found to delete.")
    

def menu():
    print("""
What would you like to do?
1. Log my mood
2. Get activity suggestion
3. View my mood history
4. Exit
5. Delete my last mood entry
""")
    return input("Enter your choice (1-5): ")