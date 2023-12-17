from pymongo import MongoClient


def migrate_data():
    try:
        # Connect to source database
        source_client = MongoClient('mongodb://localhost:27017/db_dummy_test_mongo')
        source_db = source_client['db_dummy_test_mongo']
        source_collection = source_db['users']

        # Connect to destination database
        destination_client = MongoClient('mongodb://localhost:27017/db_dummy_test_mongo_destination')
        destination_db = destination_client['db_dummy_test_mongo_destination']
        destination_collection = destination_db['users']

        # Migrate data
        documents = source_collection.find()
        for document in documents:
            destination_collection.insert_one(document)

    except Exception as e:
        print(f"An error occurred during data migration: {e}")

    finally:
        source_client.close()
        destination_client.close()
