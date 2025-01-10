from abc import ABC, abstractmethod
from collections import defaultdict

class FlightDAO(ABC):
    @abstractmethod
    def add_flight(self, flight):
        pass

    @abstractmethod
    def get_flights_from_city(self, city):
        pass


class FlightDAOImpl(FlightDAO):
    def __init__(self):
        self.flight_graph = defaultdict(list)  # Store flights as adjacency list

    def add_flight(self, flight):
        self.flight_graph[flight.source].append(flight)
        print("Successfully added Flight.")

    def get_flights_from_city(self, city):
        return self.flight_graph[city]
