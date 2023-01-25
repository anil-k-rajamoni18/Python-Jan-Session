import pymongo
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',level=logging.DEBUG)
from Utils import userData

logging.debug("Connecting to the Client")

client = pymongo.MongoClient(r"mongodb+srv://Alien:AlienDb@cluster0.mitqgvp.mongodb.net/?retryWrites=true&w=majority")

print("conecting.....")
logging.debug("fetching the database")

db = client["userprofiles"]

logging.debug("fecthing the table/collections")

collection = db["users"]

logging.debug("DB connection is successfully")

# data = [userData("Ram","Ram123") , userData("Sita","sit123"),userData("John","John123"),userData("Hemanth","Hemanth321"),userData("Ganesh","Ganesh2211")]

# logging.debug("Inserting the data")
# collection.insert_many(data)

print(dir(collection))
# fetching 
res = collection.find()

for data in res:
    print(data)
print("Success")
