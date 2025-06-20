import re
from datetime import datetime
from bson import ObjectId

class RestaurantService:
    """
    Bietet alle Logiken:
      - Stadtbezirke listen
      - Top-3 Restaurants
      - Nächstes Restaurant per Geokoordinaten
      - Suche nach Name/Küche
      - Bewertung hinzufügen
    """
    def __init__(self, collection):
        self.collection = collection

    def list_districts(self):
        districts = self.collection.distinct("borough")
        return districts

    def top3_restaurants(self):
        pipeline = [
            {"$unwind": "$grades"},
            {"$group": {
                "_id": "$name",
                "avgScore": {"$avg": "$grades.score"},
                "firstDoc": {"$first": "$$ROOT"}
            }},
            {"$sort": {"avgScore": -1}},
            {"$limit": 3},
            {"$project": {
                "_id": 0,
                "name": "$_id",
                "avgScore": 1,
                "borough": "$firstDoc.borough"
            }}
        ]
        return list(self.collection.aggregate(pipeline))

    def find_nearest_to(self, name: str):
        self.collection.create_index([("address.coord", "2dsphere")])
        src = self.collection.find_one({"name": name})
        if not src:
            return None
        coord = src["address"]["coord"]  
        cursor = self.collection.find({
            "address.coord": {
                "$near": {
                    "$geometry": {"type": "Point", "coordinates": coord}
                }
            }
        }).limit(2)
        results = list(cursor)
        return results[1] if len(results) > 1 else None

    def search_restaurants(self, name: str = None, cuisine: str = None):
        query = {}
        if name:
            query["name"] = {"$regex": re.escape(name), "$options": "i"}
        if cuisine:
            query["cuisine"] = {"$regex": re.escape(cuisine), "$options": "i"}
        return list(self.collection.find(query))

    def rate_restaurant(self, restaurant_id: str, score: float):
        oid = ObjectId(restaurant_id)
        update = {
            "$push": {
                "grades": {"date": datetime.utcnow(), "score": score}
            }
        }
        result = self.collection.update_one({"_id": oid}, update)
        return result.modified_count == 1
