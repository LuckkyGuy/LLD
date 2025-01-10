from threading import Lock

# Exception Classes
class RestaurantNotFoundException(Exception):
    pass

class BookingUnavailableException(Exception):
    pass

class SlotAlreadyBookedException(Exception):
    pass

# Entities
class Restaurant:
    def __init__(self, name, city, area, cuisine, cost_for_two, is_veg, available_slots):
        self.name = name
        self.city = city
        self.area = area
        self.cuisine = cuisine
        self.cost_for_two = cost_for_two
        self.is_veg = is_veg
        self.available_slots = available_slots # Dict[date: List[time_slots]]
        self.lock = Lock()  # To handle concurrency

    def is_available(self, date, slot):
        return date in self.available_slots and slot in self.available_slots[date]

    def book_slot(self, date, slot):
        with self.lock:
            if not self.is_available(date, slot):
                raise SlotAlreadyBookedException(f"Slot {slot} on {date} is already booked.")
            self.available_slots[date].remove(slot)

class User:
    def __init__(self, username):
        self.username = username

class Booking:
    def __init__(self, user, restaurant, date, slot):
        self.user = user
        self.restaurant = restaurant
        self.date = date
        self.slot = slot