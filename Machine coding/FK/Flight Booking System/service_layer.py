import sys, os
sys.path.append(os.path.dirname(__file__))

from threading import Lock
from entites import Flight
from strategy import FlightSearchStrategy, CheapestFlightStrategy, MinHopFlightStrategy

class FlightSearchService:
    __shared_instance = None
    __singleton_lock = Lock()
    
    @staticmethod
    def getInstance(flight_dao):
        if not FlightSearchService.__shared_instance:
            with FlightSearchService.__singleton_lock:
                if not FlightSearchService.__shared_instance:
                    FlightSearchService(flight_dao)
        return FlightSearchService.__shared_instance
    
    def __init__(self, flight_dao):
        if FlightSearchService.__shared_instance:
            raise Exception("This class is a Singleton class !")
        else:
            FlightSearchService.__shared_instance = self
            self.flight_dao = flight_dao
            self.strategy = None
            self.lock = Lock()
        
    def __set_strategy(self, strategy: FlightSearchStrategy):
        self.strategy = strategy

    def add_flight(self, airline, source, destination, price, has_meal_service=False):
        with self.lock:  # Concurrency-safe flight addition
            flight = Flight(airline, source, destination, price, has_meal_service)
            self.flight_dao.add_flight(flight)

    def find_cheapest_flight(self, source, destination, filter_options=None):
        self.__set_strategy(CheapestFlightStrategy.getInstance())
        return self.strategy.find_flight(self.flight_dao, source, destination, filter_options)
    
    def find_min_hop_flight(self,source, destination, filter_options=None):
        self.__set_strategy(MinHopFlightStrategy.getInstance())
        return self.strategy.find_flight(source, destination, filter_options)

    def _filter_flight(self, flight, filter_options):
        if filter_options and 'meal_service' in filter_options and filter_options['meal_service']:
            return flight.has_meal_service
        return True
