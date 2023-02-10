from mongoDbConnection import collection

def mongoCollection():
    res = collection.find()
    return list(res)

# mongoCollection()
def fetchOneRecord(username):
    return collection.find_one({"username":username})