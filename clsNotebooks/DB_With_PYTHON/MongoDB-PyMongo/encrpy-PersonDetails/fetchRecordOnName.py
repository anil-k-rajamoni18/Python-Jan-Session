import pymongo

import hashlib

# STEP1 Connection to client : URL

myclient = pymongo.MongoClient("mongodb+srv://Alien:AlienDB@cluster0.mitqgvp.mongodb.net/?retryWrites=true&w=majority")

# connection to the DB.

mydb = myclient["userProfiles"]

#  connection to collection

mycol = mydb["profile"]


def fetchRecordUserName(uname):
  return mycol.find_one({"name":uname})

def inputEncrypPasswd(passwd):
  return hashlib.md5(passwd.encode()).hexdigest()