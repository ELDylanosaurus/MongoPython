import bson.json_util
from pymongo import MongoClient
import bson
 
client = MongoClient('mongodb://localhost:27017')
db = client['restaurants']
collection = db['restaurants']
restaurant = 'Le Perigord'
 
def ermittle_naechstes_restaurant():
    ausgangspunkt = collection.find_one({'name': '{restaurant}'})
 
    if ausgangspunkt:
        ausgabe_json = bson.json_util.dumps(ausgangspunkt)
        print(ausgabe_json)
    else:
        print(bson.json_util.dumps({"error": "Restaurant '{restaurant}' nicht gefunden."}, indent=4))