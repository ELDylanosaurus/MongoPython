from pymongo import MongoClient

class DatabaseConnector:
    """
    Kümmert sich um die Verbindung zur MongoDB.
    Passe hier den Connection String und Datenbanknamen an.
    """
    def __init__(self,
                 connection_string: str = 'mongosh "mongodb+srv://Dylano:Informatikistcool@m165cluster.m9lf4.mongodb.net/myDatabase?retryWrites=true&w=majority" --apiVersion 1',
                 db_name: str = "restaurant_db"):
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.collection = self.db.restaurants
