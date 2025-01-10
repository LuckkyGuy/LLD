import sys, os
sys.path.append(os.path.dirname(__file__))

import datetime 
from entities import Restaurant, Booking
from entities import RestaurantNotFoundException, BookingUnavailableException, SlotAlreadyBookedException

class BookingSystem:
    def __init__(self, max_days_in_future=30):
        self.restaurants = []
        self.bookings = []
        self.max_days_in_future = max_days_in_future

    def register_restaurant(self, name, city, area, cuisine, cost_for_two, is_veg, available_slots):
        restaurant = Restaurant(name, city, area, cuisine, cost_for_two, is_veg, available_slots)
        self.restaurants.append(restaurant)

    def search_restaurants(self, **kwargs):
        filtered_restaurants = []
        for restaurant in self.restaurants:
            if all(getattr(restaurant, key) == value for key, value in kwargs.items()):
                filtered_restaurants.append(restaurant)
        return filtered_restaurants

    def book_table(self, user, restaurant_name, preferred_date, slot):
        if not isinstance(preferred_date, datetime.date) or not isinstance(slot, str):
            raise ValueError("Invalid date or slot format.")
        
        if preferred_date > datetime.datetime.now().date() + datetime.timedelta(days=self.max_days_in_future):
            raise BookingUnavailableException("Booking is not allowed for this date.")
        
        restaurant = next((r for r in self.restaurants if r.name == restaurant_name), None)
        if not restaurant:
            raise RestaurantNotFoundException(f"Restaurant {restaurant_name} not found.")
        
        restaurant.book_slot(preferred_date, slot)
        booking = Booking(user, restaurant, preferred_date, slot)
        self.bookings.append(booking)
        return booking