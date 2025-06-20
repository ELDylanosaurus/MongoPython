import re
from datetime import datetime
from pymongo import MongoClient

class RestaurantSuche:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['restaurants']
        self.collection = self.db['restaurants']

    def suche_restaurants(self, name="", cuisine=""):
        query = {}
        if name:
            query["name"] = {"$regex": name, "$options": "i"}
        if cuisine:
            query["cuisine"] = {"$regex": cuisine, "$options": "i"}
        return list(self.collection.find(query))

    def zeige_ergebnisse(self, results):
        if not results:
            print("Keine Restaurants gefunden.")
            return None
        print(f"\n{len(results)} Restaurant(s) gefunden:")
        for i, restaurant in enumerate(results, start=1):
            print(f"{i}. {restaurant.get('name', 'Unbekannt')} - {restaurant.get('cuisine', 'Unbekannt')}")
            print(f"   ID: {restaurant.get('_id')}")
        if len(results) > 1:
            try:
                choice = int(input("\nWähle ein Restaurant (Nummer): ")) - 1
                if 0 <= choice < len(results):
                    return results[choice]['_id']
                else:
                    print("Ungültige Auswahl.")
            except ValueError:
                print("Bitte eine gültige Zahl eingeben.")
            return None
        else:
            return results[0]['_id']

    def bewertung_hinzufuegen(self, restaurant_id, score, comment=""):
        new_rating = {
            "grade": "A",
            "score": score,
            "date": datetime.now(),
            "comment": comment
        }

        result = self.collection.update_one(
            {"_id": restaurant_id},
            {"$push": {"grades": new_rating}}
        )

        if result.modified_count > 0:
            print("Bewertung erfolgreich hinzugefügt!")
        else:
            print("Fehler beim Hinzufügen der Bewertung.")
        return result

class RestaurantAnwendung(RestaurantSuche):
    def restaurant_bewerten(self, restaurant_id):
        print("\nRestaurant bewerten")
        print("-" * 20)
        try:
            score = int(input("Score (1-100): "))
            if not (1 <= score <= 100):
                print("Score muss zwischen 1 und 100 liegen.")
                return
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")
            return
        comment = input("Kommentar (optional): ")
        self.bewertung_hinzufuegen(restaurant_id, score, comment)

    def suche_ausfuehren(self):
        name = input("Name (optional): ")
        cuisine = input("Küche (optional): ")
        results = self.suche_restaurants(name, cuisine)
        return self.zeige_ergebnisse(results)

    def run(self):
        while True:
            print("\n1. Restaurant suchen")
            print("2. Beenden")
            choice = input("\nAuswahl: ")
            if choice == "1":
                restaurant_id = self.suche_ausfuehren()
                if restaurant_id:
                    confirm = input("\nMöchtest du dieses Restaurant bewerten? (j/n): ").lower()
                    if confirm == 'j':
                        self.restaurant_bewerten(restaurant_id)
            elif choice == "2":
                print("Programm beendet.")
                break
            else:
                print("Ungültige Auswahl. Bitte erneut versuchen.")

if __name__ == "__main__":
    app = RestaurantAnwendung()
    app.run()
