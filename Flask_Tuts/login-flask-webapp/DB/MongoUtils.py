import pymongo 

REMOTE_DB_URL = "mongodb+srv://Alien:AlienDB@cluster0.mitqgvp.mongodb.net/?retryWrites=true&w=majority"
LOCAL_DB_URL = "mongodb://localhost:27017/"
DB_NAME = "UsersDB"
COLL_NAME = "users"

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


def insertOne():
    pass

def findOneRecord():
    pass

def updateRecord():
    pass

def removeRecord():
    pass