import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


def backup_data():
    mongo_uri = os.getenv('MONGO_URI_SOURCE', 'mongodb://localhost:27017/db_dummy_test_mongo')
    backup_dir = "C:\\mongodb_backups"

    # Run mongodump command
    os.system(f"mongodump --uri={mongo_uri} --out={backup_dir}")
    return backup_dir


def migrate_data():
    source_client = None
    destination_client = None
    try:

        mongo_uri_source = os.getenv("MONGO_URI_SOURCE")
        mongo_uri_dest = os.getenv("MONGO_URI_DEST")
        # Connect to source database
        source_client = MongoClient(mongo_uri_source)
        source_db = source_client['db_dummy_test_mongo']
        source_collection = source_db['users']

        # Connect to destination database
        destination_client = MongoClient(mongo_uri_dest)
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
