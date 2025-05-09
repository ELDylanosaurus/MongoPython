from pymongo import MongoClient

connection_string = "mongodb+srv://Dylano:123@m165cluster.m9lf4.mongodb.net/"
client = MongoClient(connection_string)

dblist = client.list_database_names()

for db in dblist:
	print(db)

dblist = client.list_database_names()

if "admin" in dblist:
    print("Database exists.")
else:
    print("Database does not exist.")

db = client["inf"]  