from collections import defaultdict
import sys, os
sys.path.append(os.path.dirname(__file__))

from sortedcontainers import SortedList 

class Restaurant:
    def __init__(self, id, name, city, area, cusine, restaurant_type, cost_for_two):
        self.id = id
        self.name = name
        self.city = city
        self.area = area
        self.cusine = cusine
        self.restaurant_type = restaurant_type
        self.cost_for_two = cost_for_two        
        self.availability = defaultdict(lambda : SortedList())

    def booking_request(self, date, timing):
        for start, end in self.availability[date.__str__()]:
            if timing in self.availability[date.__str__()]:
                print("Can't book the table for givem time as it is already booked by other.")
                return
        self.availability[date.__str__()].add(timing)
        print("Booked given request successfully.")

    def __str__(self):
        return f"{self.name} Resturant located at {self.area}."


class SearchParam:
    def __init__(self):
        self.name = None
        self.city = None
        self.area = None
        self.cusine = None
        self.restaurant_type = None
        