from abc import ABC, abstractmethod
from heapq import heappop, heappush
from collections import defaultdict

class FlightSearchStrategy(ABC):
    @abstractmethod
    def find_flight(self, flight_dao, source,destination, filter_options=None):
        pass

class CheapestFlightStrategy(FlightSearchStrategy):
    __shared_instance = None
    
    @staticmethod
    def getInstance():
        if not CheapestFlightStrategy.__shared_instance:
            CheapestFlightStrategy()
        return CheapestFlightStrategy.__shared_instance
    
    def __init__(self):
        if CheapestFlightStrategy.__shared_instance:
            raise Exception("This class is a Singleton class !")
        else:
            CheapestFlightStrategy.__shared_instance = self

    def find_flight(self,flight_dao, source, destination, filter_options= None):
        # print(f"Finding the cheapest flight from {source.code} to {destination.code} with filters: {filter_options}")
        hp = [(0, 0, source)]
        cost = defaultdict(lambda : float('inf'))
        flight_hop = defaultdict(lambda : float('inf'))
        cost[source] = 0
        flight_hop[source] = 0
        while hp:
            curr_cost, hop, node = heappop(hp)
            for flight in flight_dao.flight_graph[node]:
                if ((curr_cost + flight.price) < cost[flight.destination]) or ((curr_cost + flight.price) == cost[flight.destination] and flight_hop[flight.destination] > hop+1):
                    cost[flight.destination] = curr_cost + flight.price
                    flight_hop[flight.destination] = hop+1
                    heappush(hp, (cost[flight.destination], hop+1, flight.destination))
        
        return cost[destination], flight_hop[destination]

class MinHopFlightStrategy(FlightSearchStrategy):
    __shared_instance = None
    
    @staticmethod
    def getInstance():
        if not MinHopFlightStrategy.__shared_instance:
            MinHopFlightStrategy()
        return MinHopFlightStrategy.__shared_instance
    
    def __init__(self):
        if MinHopFlightStrategy.__shared_instance:
            raise Exception("This class is a Singleton class !")
        else:
            MinHopFlightStrategy.__shared_instance = self

    def find_flight(self, source, destination,filter_options=None):
        # print(f"Finding the  minimum hop flight from {source.code} to {destination.code} with filters: {filter_options}")
        # The actual algorithm would go here.
        return
