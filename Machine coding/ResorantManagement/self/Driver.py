import sys, os, datetime
sys.path.append(os.path.dirname(__file__))

from restaurantManagement import RestaurantManagement
from entities import SearchParam

def main():
    system = RestaurantManagement()
    system.registerRestaurant(1, "Rameshawarm", "Bangalore", "Whitefield", "Sweet", "NonVeg", 500)
    system.registerRestaurant(2, "Dhaba", "Bangalore", "SitaramPalya", "Sweet", "veg", 1000)

    searchParam = SearchParam()
    searchParam.name = "Rameshawarm"
    searchParam.city = "Bangalore"

    print("### Searchuing restaurants ###")
    system.search_restaurant(searchParam)
    print("### Searchuing restaurant ###")


    # assuming user we are able to get the date and time from UI in required format
    date = datetime.date(2024, 9, 4)
    time = (6, 7)
    system.book_table(1, date, time)
    system.book_table(1, date, time)
    
    # time = datetime.time()
    # time = (7, 8) 
    # system.book_table()
    

if __name__ == '__main__':
    main()
