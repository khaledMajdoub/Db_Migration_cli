from pymongo import MongoClient

# Initialize two MongoDB clients
source_client = MongoClient('mongodb://localhost:27017/db_dummy_test_mongo')
destination_client = MongoClient('mongodb://localhost:27017/db_dummy_test_mongo_dest')

source_db = source_client['db_dummy_test_mongo']
destination_db = destination_client['db_dummy_test_mongo_dest']

source_collection = source_db['users']
destination_collection = destination_db['users']


def migrate_data():
    documents = source_collection.find()

    for document in documents:
        destination_collection.insert_one(document)

    source_client.close()
    destination_client.close()
