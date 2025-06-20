from room import Room
from verwalter import RaumVerwalter
 
verwalter = RaumVerwalter("mongodb://localhost:27017/")
 
raum_create = Room("Pilatus", 12, True)
verwalter.create(raum_create)
 
raum_read = verwalter.read()
print("Gelesener Raum:")
print(vars(raum_read))  
 
if hasattr(raum_read, "_id"):
    updated_room = Room("Titlis", 20, False)
    verwalter.update(raum_read._id, updated_room)
    print("Raum aktualisiert.")
 
raum_updated = verwalter.read()
print("Aktualisierter Raum:")
print(vars(raum_updated))
 
if hasattr(raum_updated, "_id"):
    verwalter.delete(raum_updated._id)
    print("Raum gelöscht.")