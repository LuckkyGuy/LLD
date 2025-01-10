class Flight:
    def __init__(self, airline, source, destination, price, has_meal_service=False):
        self.airline = airline
        self.source = source
        self.destination = destination
        self.price = price
        self.has_meal_service = has_meal_service

    def __repr__(self):
        return f"{self.source} to {self.destination} via {self.airline} for {self.price}"

class Airline:
    def __init__(self, name):
        self.name = name
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)