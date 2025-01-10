import sys, os
sys.path.append(os.path.dirname(__file__))

from entity import User, Center
from datetime import datetime, timedelta


class FlitnessSystem:
    __shared_instance = None
    
    # singleton class
    @staticmethod
    def getInstance(weekly_limit):
        if not FlitnessSystem.__shared_instance:
            FlitnessSystem(weekly_limit)
        return FlitnessSystem.__shared_instance
    
    def __init__(self, weekly_limit):
        if FlitnessSystem.__shared_instance:
            raise Exception("This class is a Singleton class !")
        else:
            FlitnessSystem.__shared_instance = self
            self.users = {}  # {email: User}
            self.centers = {}  # {center_name: Center}
            self.weekly_limit = weekly_limit  # Admin-defined weekly workout limit
            self.distance_metrics = {
                'Koramangala' : {'Koramangala':0, 'Bellandur': 5},
                'Bellandur' : {'Koramangala':5, 'Bellandur': 0},
            }
        

    def register_user(self, name, email, location):
        if email not in self.users:
            self.users[email] = User(name, email, location)
            print(f"User {name} registered successfully!")
        else:
            print(f"User with email {email} already exists.")
    
    def add_center(self, center_name):
        if center_name not in self.centers:
            self.centers[center_name] = Center(center_name)
            print(f"Hey, Center {center_name} added.")
        else:
            print(f"Hey, Center {center_name} is already added.")
    
    def add_workout(self, center_name, workout_type, start_time, end_time, capacity , start_date, end_date):
        if center_name in self.centers:
            self.centers[center_name].add_workout(workout_type, start_time, end_time, capacity, start_date, end_date)
            print(f"Workout {workout_type} added to {center_name} from {start_date} to {end_date}")
        else:
            print(f"Center {center_name} not found.")
    
    def view_workout_slot_availability(self, email_id, workout_type, date):
        print(f"Workout availability for {workout_type} on {date}:")

        user = self.users[email_id]
        user_location = user.location
        centers = sorted(self.centers.items(), lambda x: self.distance_metrics[user_location][x[0]])

        for center_name, center in centers:
            slots = center.get_filtered_slots(date, workout_type)
            if slots:
                print(f"Center: {center_name}")
                for slot in slots:
                    print(slot)
    
    def book_session(self, email, center_name, workout_type, start_time, end_time, date):
        if email not in self.users:
            print(f"User {email} is not registered.")
            return
        if center_name not in self.centers:
            print(f"Center {center_name} not found.")
            return
        
        user = self.users[email]
        center = self.centers[center_name]

        # Check if user has exceeded weekly limit
        booking_date = datetime.strptime(date, "%d-%m-%y")
        week_start = self._get_start_of_week(booking_date)
        weekly_bookings = user.get_weekly_booking_count(week_start)

        if weekly_bookings >= self.weekly_limit:
            print(f"User {email} has already reached the weekly limit of {self.weekly_limit} bookings")
            return

        slots = center.get_filtered_slots(date, workout_type)
        for slot in slots:
            if slot.start_time == start_time and slot.end_time == end_time:
                if slot.book_slot():
                    self.users[email].bookings.append((center_name, workout_type, start_time, end_time, date))
                    print(f"Session booked successfully for {email} at {center_name} on {date}.")
                else:
                    print(f"No seats available for {workout_type} at {center_name} on {date}.")
                return
        print(f"No matching workout found.")
    
    def view_schedule(self, email, date, workout_type=None, center_name=None):
        if email not in self.users:
            print(f"User {email} is not registered.")
            return
        
        print(f"Schedule for {email} on {date}:")
        if center_name and center_name in self.centers:
            self._print_center_schedule(self.centers[center_name], date, workout_type)
        else:
            for center in self.centers.values():
                self._print_center_schedule(center, date, workout_type)
    
    def _print_center_schedule(self, center, date, workout_type=None):
        if date not in center.workout_slots:
            print(f"No slots available on {date} for center {center.name}")
            return
        
        slots = center.get_filtered_slots(date, workout_type)
        
        if slots:
            print(f"Center: {center.name}")
            for slot in slots:
                print(slot)
    
    # Helper function to get the start of the week for a given date
    def _get_start_of_week(self, date):
        weekday = date.weekday()  # Monday is 0
        start_of_week = date - timedelta(days=weekday)
        return start_of_week
