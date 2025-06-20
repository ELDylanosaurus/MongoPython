from pymongo import MongoClient
from datetime import datetime
from math import radians, sin, cos, sqrt, atan2

client = MongoClient("mongodb://localhost:27017/")
db = client["restaurants"]
collection = db["restaurants"]

boroughs = collection.distinct("borough")
print("Stadtbezirke:", boroughs)

pipeline = [
    {"$unwind": "$grades"},
    {"$group": {
        "_id": "$name",
        "avgScore": {"$avg": "$grades.score"}
    }},
    {"$sort": {"avgScore": -1}},
    {"$limit": 3}
]
top3 = list(collection.aggregate(pipeline))
print("Top 3:", top3)

target = collection.find_one({"name": "Le Perigord"})
if target and "address" in target and "coord" in target["address"]:
    lon1, lat1 = target["address"]["coord"]
    def distance(r):
        try:
            lon2, lat2 = r["address"]["coord"]
            phi1, phi2 = radians(lat1), radians(lat2)
            dphi = radians(lat2 - lat1)
            dlambda = radians(lon2 - lon1)
            a = sin(dphi / 2)**2 + cos(phi1) * cos(phi2) * sin(dlambda / 2)**2
            return 6371 * 2 * atan2(sqrt(a), sqrt(1 - a))
        except:
            return float("inf")
    others = list(collection.find({"name": {"$ne": "Le Perigord"}}))
    nearest = min(others, key=distance)
    print("Nächstes zu Le Perigord:", nearest["name"])
