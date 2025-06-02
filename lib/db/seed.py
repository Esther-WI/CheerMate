from faker import Faker
from lib.db.models import User, Mood , Activity, session
import random

fake = Faker()

session.query(User).delete()
session.query(Mood).delete()
session.query(Activity).delete()
session.commit()

users = [
    User(
        username=fake.user_name(),
        gender = random.choice(["Male", "Female"]),
        email= fake.email()
          )
            for _ in range(5)
]
session.add_all(users)
session.commit()

mood_feelings = ["Happy", "Sad", "Anxious", "Motivated", "Frustrated"]
moods = [
    Mood(
        feeling = feeling,
        user_id = random.choice(users).id
    )
    for feeling in mood_feelings

]
session.add_all(moods)
session.commit()

activities = [
    Activity(mood_trigger="Happy", suggestion="Dance to your favorite song"),
    Activity(mood_trigger="Sad", suggestion="Watch a funny movie"),
    Activity(mood_trigger="Anxious", suggestion="Try deep breathing"),
    Activity(mood_trigger="Motivated", suggestion="Start a new project"),
    Activity(mood_trigger="Frustrated", suggestion="Take a short walk"),
]
session.add_all(activities)
session.commit()
print("Database seeded successfully!")



