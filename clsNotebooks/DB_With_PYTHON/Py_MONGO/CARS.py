import pymongo 

def CreateConnection(db_name,coll_name):
    DB_URL = "mongodb://localhost:27017/"
    #client connection 
    client = pymongo.MongoClient(DB_URL)

    #DB CONNECTION
    my_db = client[db_name]

    #COLLECTION connection 
    my_coll = my_db[coll_name]
    return my_coll


def ReadData():
    import json
    
    #f = open("CARS.json")
    #data = json.load(f)
    import requests 
    data = requests.get("https://raw.githubusercontent.com/vega/vega/main/docs/data/cars.json")
    data = data.json()
    return data
    
def InsertData(coll,data):
    for dt in data:
        coll.insert_one(dt)
    return "data inserted successfully..."


def filterData(coll):
    return coll.find_one()