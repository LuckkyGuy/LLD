# https://docs.google.com/document/d/1alUGxE3Z751PDv1qX2ozD0YTn8DD6Tlw/edit

import sys, os
sys.path.append(os.path.dirname(__file__))

from FitnessSystem import FlitnessSystem

# Example Usage
weekly_limit = 3  # Admin sets a limit of 3 workouts per week
flitness = FlitnessSystem.getInstance(weekly_limit)

# Register Users
flitness.register_user("Yash", "yash@example.com", "Koramangala")
flitness.register_user("Manoj", "manoj@example.com", "Bellandur")

# Adding Centers
print("------------")
flitness.add_center("Koramangala")
flitness.add_center("Koramangala")
flitness.add_center("Bellandur")


# Admin adds workout sessions
print("------------")
flitness.add_workout("Koramangala", "Weights", 6, 7, 10, "01-09-24", "30-09-24")
flitness.add_workout("Bellandur", "Yoga", 7, 8, 8, "01-09-24", "30-09-24")
flitness.add_workout("Bellandur", "Weights", 7, 8, 8, "01-09-24", "30-09-24")

# User views workout availability
print("------------")
flitness.view_workout_slot_availability("Weights", "20-09-24")

# User books a session
print("------------")
flitness.book_session("yash@example.com", "Koramangala", "Weights", 6, 7, "20-09-24")

# View schedule
print("------------")
# flitness.view_schedule("yash@example.com", "20-09-24")
flitness.view_schedule("yash@example.com", "20-09-24", "Weights")
