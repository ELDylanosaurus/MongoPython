from pymongo import MongoClient
from room import Room
from bson.objectid import ObjectId
 
class RaumVerwalter:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.col = MongoClient(connection_string)["buildings"]["rooms"]
 
    def erstellen(self, room):
        self.col.insert_one(room.__dict__)
 
    def lesen(self):
        room_data = self.col.find_one()
        if room_data:
            return Room(**room_data)
        return None
 
    def aktualisieren(self, room_id, aktualisierend_room):
        self.col.aktualisieren_one(
            {"_id": ObjectId(room_id)},
            {"$set": {
                "name": aktualisierend_room.name,
                "seats": aktualisierend_room.seats,
                "is_reservable": aktualisierend_room.is_reservable
            }}
        )
 
    def loeschen(self, room_id):
        self.col.loeschen_one({"_id": ObjectId(room_id)})