import pymongo

localDB_URL = "mongodb://localhost:27017/"

remoteDB_URL = "mongodb+srv://Alien:AlienDB@cluster0.mitqgvp.mongodb.net/?retryWrites=true&w=majority"

# connection to the client

client = pymongo.MongoClient(remoteDB_URL)


print(client.list_database_names())

# 2. making connection to DB

mydb = client["COURSES"]

print(mydb.list_collection_names())

# 3.make a connection to the collection.

mycol = mydb["course"]

result = mycol.find({"name":"Dart"},{"name":1,"fee":1})

for data in result:
  print(data)