import sys, os
sys.path.append(os.path.dirname(__file__))

from datetime import datetime
from entities import User
from retaurantManagement import BookingSystem

# Example Usage
if __name__ == "__main__":
    booking_system = BookingSystem()
    
    # Register restaurants
    booking_system.register_restaurant(
        name="The Food Place", 
        city="New York", 
        area="Manhattan", 
        cuisine="Italian", 
        cost_for_two=100, 
        is_veg=False,
        available_slots={
            datetime.now().date(): ["12:00", "13:00", "14:00"]
        }
    )
    
    # Search restaurants
    user = User(username="john_doe")
    restaurants = booking_system.search_restaurants(city="New York", area="Manhattan")
    for restaurant in restaurants:
        print(restaurant.name)

    # Book a table
    try:
        
        booking = booking_system.book_table(user, "The Food Place", datetime.now().date(), "12:00")
        print(f"Booking confirmed for {booking.restaurant.name} on {booking.date} at {booking.slot}")
        pass
    except Exception as e:
        print(str(e))    