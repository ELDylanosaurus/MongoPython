from pymongo import MongoClient
from test_queries import get_top_rated_restaurants, get_unique_boroughs, find_nearest_restaurant
 
def start_app():
    verbindung = MongoClient('mongodb://localhost:27017')
    db = verbindung['db_restaurants']
    sammlung = db['restaurants']
 
    print("Einzigartige Boroughs:")
    get_unique_boroughs()
 
    print("\nTop-bewertete Restaurants:")
    get_top_rated_restaurants()
 
    print("\nDas naheste Restaurant zu Le Perigord")
    find_nearest_restaurant()
    verbindung.close()
 
if __name__ == "__start_app__":
    start_app()