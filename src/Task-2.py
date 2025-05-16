databases = {
    "db1": {
        "col1": {
            "63dd4f4": {"content1": "test1", "content2": 100},
            "63dd4f5": {"content1": "test2", "content2": 200},
        },
        "col2": {},
    },
    "db2": {},
}

def show_databases(databases):
    if not databases:
        print("No Database")
        return None
    print("Databases")
    for db in databases:
        print(f" - {db}")
    return True

def select_database(databases):
    while True:
        db_name = input("Select Database: ")
        if db_name not in databases:
            print("Database not found. Try again.")
            continue
        return db_name

def show_collections(db_name, databases):
    collections = databases[db_name]
    if not collections:
        print("No Collections")
        return None
    print(f"\n{db_name}")
    print("Collections")
    for col in collections:
        print(f" - {col}")
    return True

show_databases(databases)
db_name = select_database(databases)
show_collections(db_name, databases)
