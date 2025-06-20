from test_queries import top_bewertete_restaurants, einzigartige_bezirke, finde_naechstes_restaurant
from pymongo import MongoClient

def start_app():
    verbindung = MongoClient('mongodb://localhost:27017')
    db = verbindung['db_restaurants']
    sammlung = db['restaurants']

    print("Einzigartige Boroughs:")
    einzigartige_bezirke()

    print("\nTop-bewertete Restaurants:")
    top_bewertete_restaurants()

    print("\nDas naheste Restaurant zu Le Perigord")
    finde_naechstes_restaurant()

    verbindung.close()

if __name__ == "__main__":
    start_app()
