from entities import Restaurant
import datetime    


class RestaurantManagement:
    def __init__(self):
        self.restaurants = dict()
        self.advance_booking_limit = 5


    def registerRestaurant(self, id, name, city, area, cusine, restaurant_type, cost_for_two):
        new_restaurant = Restaurant(id, name, city, area, cusine, restaurant_type, cost_for_two)
        self.restaurants[id] = new_restaurant
    
    def search_restaurant(self, searchParam):
        for restaurant in self.restaurants.values():
            if searchParam.name and searchParam.name!= restaurant.name:
                continue
            if searchParam.city and searchParam.city!= restaurant.city:
                continue
            print(restaurant)
    
    def book_table(self, id, date, time):
        day_diff = (date-datetime.date.today()).days
        if not 0<=day_diff<=self.advance_booking_limit:
            print("You can't book table beyond advance booking limit!")
            return
        restaurant = self.restaurants[id]
        restaurant.booking_request(date, time)
        

    def Show_all_restaurants(self):
        for restaurant in self.restaurants.values():
            print(restaurant)