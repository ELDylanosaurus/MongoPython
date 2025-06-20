from database_connector import DatabaseConnector
from restaurant_service import RestaurantService

class RestaurantCLI:
    """
    Einfaches CLI-Interface, das den Service nutzt.
    """
    def __init__(self, connection_string=None):
        self.db = DatabaseConnector(connection_string).collection
        self.service = RestaurantService(self.db)
        self.last_selected_id = None

    def run(self):
        while True:
            print("\nMenü:")
            print("1. Stadtbezirke anzeigen")
            print("2. Top 3 Restaurants nach Rating")
            print("3. Nächstes Restaurant zu 'Le Perigord'")
            print("4. Restaurants suchen")
            print("5. Restaurant bewerten")
            print("0. Beenden")
            choice = input("Auswahl: ").strip()

            if choice == "1":
                for b in self.service.list_districts():
                    print(f"- {b}")

            elif choice == "2":
                for doc in self.service.top3_restaurants():
                    print(f"- {doc['name']}: {doc['avgScore']:.2f} ({doc['borough']})")

            elif choice == "3":
                nearest = self.service.find_nearest_to("Le Perigord")
                if nearest:
                    print(f"Nächstes Restaurant: {nearest['name']} (ID: {nearest['_id']})")
                else:
                    print("Kein Restaurant gefunden oder kein Nachbar vorhanden.")

            elif choice == "4":
                name = input("Name (leer = ignorieren): ").strip() or None
                cuisine = input("Küche (leer = ignorieren): ").strip() or None
                results = self.service.search_restaurants(name, cuisine)
                if not results:
                    print("Keine Restaurants gefunden.")
                    continue
                for idx, r in enumerate(results, 1):
                    print(f"{idx}. {r['name']} ({r.get('cuisine','-')}) - ID: {r['_id']}")
                sel = 0
                if len(results) > 1:
                    try:
                        sel = int(input("Nummer auswählen: ")) - 1
                    except:
                        sel = 0
                self.last_selected_id = str(results[sel]["_id"])
                print(f"Ausgewählt: {results[sel]['name']}")

            elif choice == "5":
                rid = self.last_selected_id or input("Restaurant-ID eingeben: ").strip()
                try:
                    score = float(input("Bewertung (Zahl): "))
                except ValueError:
                    print("Ungültige Bewertung.")
                    continue
                if self.service.rate_restaurant(rid, score):
                    print("Bewertung erfolgreich hinzugefügt.")
                else:
                    print("Fehler beim Hinzufügen der Bewertung.")

            elif choice == "0":
                print("Programm beendet.")
                break

            else:
                print("Ungültige Auswahl, bitte erneut.")

if __name__ == "__main__":
    cli = RestaurantCLI()
    cli.run()
