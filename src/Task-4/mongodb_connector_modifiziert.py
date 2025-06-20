import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
 
def verbindung_testen_mongodb():
 
    load_dotenv()
    verbindungsadresse = os.environ.get("MONGO_URI")
    if not verbindungsadresse:
        print("Hinweis: MONGO_URI nicht gesetzt.")
        print("Bitte setzen Sie die Umgebungsvariable mit einem gültigen MongoDB Connection-String.")
        return False
    try:
        verbindung = MongoClient(verbindungsadresse, serverSelectionTimeoutMS=5000)
        verbindung.admin.command('ping')
        print("MongoDB-Verbindung erfolgreich hergestellt.")
        print(f"Server-Informationen: {verbindung.server_info()}")
        databases = verbindung.list_database_names()
        print(f"Verfügbare Datenbanken: {', '.join(databases)}")
        return True
    except ConnectionFailure as e:
        print(f"Fehler bei der Verbindung zur MongoDB: {e}")
        return False
    except Exception as e:
        print(f"Unerwarteter Fehler: {e}")
        return False
    finally:
        if 'verbindung' in locals():
            verbindung.close()
            print("MongoDB-Client getrennt.")
 
if __name__ == "__main__":
    verbindung_testen_mongodb()

 
