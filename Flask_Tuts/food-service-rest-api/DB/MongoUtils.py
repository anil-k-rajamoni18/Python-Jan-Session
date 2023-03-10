import pymongo 

REMOTE_DB_URL = "mongodb+srv://Alien:AlienDB@cluster0.mitqgvp.mongodb.net/?retryWrites=true&w=majority"
LOCAL_DB_URL = "mongodb://localhost:27017/"
DB_NAME = "FOOD"
COLL_NAME = "fooditems"

def CreateConnection():
    
    #client connection 
    try:
        client = pymongo.MongoClient(REMOTE_DB_URL)
        try:
            if DB_NAME in client.list_database_names():
                my_db = client[DB_NAME]
                try:
                    if COLL_NAME in my_db.list_collection_names():
                        my_coll = my_db[COLL_NAME]
                        print(f"Connection CREATED for {DB_NAME} &  collection {COLL_NAME} ....")
                        return my_coll
                    else:
                        raise Exception("Collection not found...")
                except Exception as e:
                    print(e)               
            else:
                raise Exception("DB NOT FOUND")
        except Exception as e:
            print(e)
        
    except Exception as e:
        print("unable to create Client connection...",e)


def insertBlukData(coll,data):
  coll.insert_many(data)
  return "inserted successfully..."


def findByUserName(coll,uname):
  return coll.find_one({"username":uname})


def findAllRecords(coll):
    apiResponse = list(coll.find({},{"_id":0}))
    return {"count": len(apiResponse) ,"foodItems" : apiResponse}

def insertOne(coll,data):
    insertResponse = coll.insert_one(data)
    print(insertResponse)
    return {"acknowledged" : insertResponse.acknowledged , "inserted_id" : str(insertResponse.inserted_id)}


def insertMany(coll,data):
    apiResponse = coll.insert_many(data)
    return {"acknowledged" : apiResponse.acknowledged , "inserted_count" : len(data)}

def findOneRecord(coll):
    return {"foodItem" : coll.find_one({},{"_id":0})}

def updateRecord():
    pass

def removeRecord():
    pass