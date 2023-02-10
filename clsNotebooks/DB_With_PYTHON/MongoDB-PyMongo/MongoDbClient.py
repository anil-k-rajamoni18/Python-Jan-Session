import pymongo

# STEP1 Connection to client : URL

myclient = pymongo.MongoClient("mongodb+srv://Alien:AlienDB@cluster0.mitqgvp.mongodb.net/?retryWrites=true&w=majority")

# connection to the DB.

mydb = myclient["STUDENT"]

dblist = myclient.list_database_names()

print(dblist)

if "STUDENT" in dblist:
  print("The database exists.")
else:
  print("The database not exist.")

#  make connection to the collection

mycol = mydb["stu"]

mydict = { "name": "John", "address": "Highway 37" }

#  insert record.

x = mycol.insert_one(mydict)

print(x)

for ch in mycol.find():
  print(ch)


