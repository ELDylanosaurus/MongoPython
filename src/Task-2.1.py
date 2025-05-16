databases = {
    "db1": {
        "col1": {
            "63dd4f4": {"content1": "test", "content2": 605},
            "63dd4f5": {"content1": "test2", "content2": 504},
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

show_databases(databases)
