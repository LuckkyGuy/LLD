from datetime import datetime, timedelta
from collections import defaultdict


class User:
    def __init__(self, name, email, location):
        self.name = name
        self.email = email
        self.location = location
        self.bookings = []

    def get_weekly_booking_count(self, week_start):
        """Returns the number of bookings for the user in the current week."""
        count = 0
        for booking in self.bookings:
            booking_date = datetime.strptime(booking[-1], "%d-%m-%y")
            if week_start <= booking_date < (week_start + timedelta(days=7)):
                count += 1
        return count


class WorkoutSlot:
    def __init__(self, workout_type, start_time, end_time, capacity, date):
        self.workout_type = workout_type
        self.start_time = start_time
        self.end_time = end_time
        self.capacity = capacity
        self.booked = 0  # number of bookings.
        self.date = date
    
    def is_available(self):
        return self.booked < self.capacity
    
    def book_slot(self):
        if self.is_available():
            self.booked += 1
            return True
        return False
    
    def __str__(self):
        return f"{self.workout_type} ({self.start_time}-{self.end_time}) - Seats Available: {self.capacity - self.booked}/{self.capacity}"


class Center:
    def __init__(self, name):
        self.name = name
        self.workout_slots = defaultdict(list)  # {date: [workout_slots]}

    def add_workout(self, workout_type, start_time, end_time, capacity, start_date, end_date):
        current_date = datetime.strptime(start_date, "%d-%m-%y")
        end_date = datetime.strptime(end_date, "%d-%m-%y")
        while current_date <= end_date:
            date_str = current_date.strftime("%d-%m-%y")
            slot = WorkoutSlot(workout_type, start_time, end_time, capacity, date_str)
            # check new slot is overlapping or not
            self.workout_slots[date_str].append(slot)
            current_date += timedelta(days=1)
    
    def get_filtered_slots(self, date, workout_type = None):
        filtered_slot = self.workout_slots[date]
        if workout_type:
            filtered_slot = [slot for slot in filtered_slot if slot.workout_type == workout_type]
        return filtered_slot

