# import sys, os
# sys.path.append(os.path.dirname(__file__))
# from entites import City
# from DAO_layer import FlightDAOImpl
# from service_layer import FlightSearchService

# def setup_flight_data(flight_search_service):
#     delhi = City('DEL')
#     bangalore = City('BLR')
#     new_york = City('NYC')
#     london = City('LON')

#     flight_search_service.add_flight('JetAir', 'DEL', 'BLR', 500)
#     flight_search_service.add_flight('Delta', 'BLR', 'LON', 1000)
#     flight_search_service.add_flight('Delta', 'LON', 'NYC', 2000)
#     flight_search_service.add_flight('Delta', 'DEL', 'NYC', 3500)
#     flight_search_service.add_flight('JetAir', 'DEL', 'LON', 2000)

# # Instantiate the DAO and the FlightSearchService
# flight_dao = FlightDAOImpl()
# flight_search_service = FlightSearchService(flight_dao)

# setup_flight_data(flight_search_service)

# source = 'DEL'
# destination = 'NYC'
# filter_options = {'meal_service' : True}

# # Minimum cost flight
# flight_search_service.find_cheapest_flight(source, destination, filter_options)

# # Minimum hop flight
# flight_search_service.find_min_hop_flight(source, destination, filter_options)


from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    print(f"Task {n} started")
    time.sleep(2)
    return f"Task {n} completed"

# Create a ThreadPoolExecutor with 3 threads
with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks to the pool
    futures = [executor.submit(task, i) for i in range(5)]
    
    # Get results as they complete
    for future in futures:
        print(future.result())
