from faker import Faker
from models import User, Mood , Activity, session
import random

fake = Faker()

session.query(User).delete()
session.query(Mood).delete()
session.query(Activity).delete()

users = [User
         (username=fake.user_name(),
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
        feeling = random.choice(mood_feelings),
        user_id = random.choice(users).id
    )
    for _ in range(10)

]
session.add_all(moods)
session.commit()

activities = [
    Activity(
        mood_trigger=random.choice(mood_feelings),
        suggestion=random.choice([
            "Take a walk", 
            "Listen to calming music", 
            "Write in a journal", 
            "Call a friend", 
            "Meditate"
        ]),
        user_id=random.choice(users).id
    )
    for _ in range(10)
]
session.add_all(activities)
session.commit()
print("Database seeded successfully!")



