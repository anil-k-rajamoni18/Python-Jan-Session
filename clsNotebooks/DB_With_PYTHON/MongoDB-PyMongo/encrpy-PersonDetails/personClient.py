import pymongo
from hashlibUtil import encrpyData
# STEP1 Connection to client : URL

myclient = pymongo.MongoClient("mongodb+srv://Alien:AlienDB@cluster0.mitqgvp.mongodb.net/?retryWrites=true&w=majority")

# connection to the DB.

mydb = myclient["userProfiles"]

#  connection to collection

mycol = mydb["profile"]


data = [{"name": "Kumar","email":"kumar@gmail.com","passwd":"Kumar123"},
{"name": "Rajamoni","email":"Rajamoni@gmail.com","passwd":"Rajamoni123"},
{"name": "Lavanya","email":"lavanya@yahoo.com","passwd":"lavaya@123"},
{"name": "rashmi","email":"rashmi@yahoo.com","passwd":"rashmi#123"}]

# deleted existing documents 


mycol.delete_many({})


# encrypasswd.
encryptedData = encrpyData(data)

if encryptedData:
  response = mycol.insert_many(encryptedData)
  print(response.inserted_ids)
else:
  print("data is empty")


