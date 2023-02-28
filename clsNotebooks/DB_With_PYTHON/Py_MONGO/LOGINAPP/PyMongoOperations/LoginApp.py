from MongoUtils import createDBCollection,findByUserName,insertBlukData,CreateConnection;
from CommonUtils import *;

if __name__ == '__main__':
  print("connectin......")
  DB_NAME = input("Enter DATABASE name: ")
  COLL_NAME = input("Enter COLLECTION name: ")

  REMOTE_DB_URL = "mongodb+srv://Alien:AlienDB@cluster0.mitqgvp.mongodb.net/?retryWrites=true&w=majority"
  LOCAL_DB_URL = "mongodb://localhost:27017/"
  FILE_NAME = "USERSDATA.json"

  # print(createDBCollection(DB_NAME,COLL_NAME,REMOTE_DB_URL))

  coll = CreateConnection(DB_NAME,COLL_NAME,REMOTE_DB_URL)

  # encryptedData = readDataFromFileName(FILE_NAME)

  # print(insertBlukData(coll,encryptedData))

  usernameInp = input("ENTER USERNAME :  ")
  
  response_Data = findByUserName(coll,usernameInp)
  print(response_Data)
  if response_Data:
    if response_Data["username"] == usernameInp:
      passwordInp = input("ENTER PASSWORD :  ")
      if response_Data["password"] == encrypt(passwordInp):
        print("LOGIN SUCCESS")
      else:
        print("INVALID PASSWORD....")
    else:
      print("INVALID USERNAME...")
  else:
    print("NO MATCHING RECORD OR USERNAME....")

  

