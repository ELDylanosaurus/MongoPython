import time

mock_db = {
    "Testdb1": {
        "col1": {
            "63dd4f4": {"Testtest": "test1", "test2": 101},
            "63dd4f5": {"Wert": "wert 1", "wert2": 102}
        },
        "Testcol2": {}
    },
    "Testdb2": {
        "col1": {
            "63dd4f6": {"content1": "example3", "content2": 103}
        }
    },
    "Testdb3": {}
}

def show_databases():
    print("\nDatabases")
    if not mock_db:
        print("No Database")
        return None
    for db in mock_db:
        print(f" - {db}")
    db_choice = input("\nSelect Database: ")
    if db_choice not in mock_db:
        print("Database not found. Try again.")
        return show_databases()
    return db_choice

def show_collections(db_name):
    collections = mock_db[db_name]
    print(f"\n{db_name}\n\nCollections")
    if not collections:
        print("No Collection\n")
        input("Press any button to return")
        return None
    for col in collections:
        print(f" - {col}")
    col_choice = input("\nSelect Collection: ")
    if col_choice not in collections:
        print("Collection not found. Try again.")
        return show_collections(db_name)
    return col_choice

def show_documents(db_name, col_name):
    documents = mock_db[db_name][col_name]
    print(f"\n{db_name}.{col_name}\n\nDocuments")
    if not documents:
        print("No Document\n")
        input("Press any button to return")
        return None
    for doc_id in documents:
        print(f" - {doc_id}")
    doc_choice = input("\nSelect Document: ")
    if doc_choice not in documents:
        print("Document not found. Try again.")
        return show_documents(db_name, col_name)
    return doc_choice

def show_document_content(db_name, col_name, doc_id):
    content = mock_db[db_name][col_name][doc_id]
    print(f"\n{db_name}.{col_name}.{doc_id}")
    for key, value in content.items():
        print(f"{key}: {value}")
    input("\nPress any button to return")

def main():
    while True:
        db_name = show_databases()
        if db_name is None:
            input("Press any button to return")
            continue

        col_name = show_collections(db_name)
        if col_name is None:
            continue

        doc_id = show_documents(db_name, col_name)
        if doc_id is None:
            continue

        show_document_content(db_name, col_name, doc_id)

if __name__ == "__main__":
    main()
