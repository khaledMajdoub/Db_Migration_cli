from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/db_dummy_test_mongo')

db = client['db_dummy_test_mongo']
collection = db['users']

document = {"name": "Ridha", "age": 30}
collection.insert_one(document)

result = collection.find_one({"name": "Ridha"})
print(result)

client.close()
