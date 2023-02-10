from fetchRecordOnName import *

uname = input('Enter the username: ')

dbRecord = fetchRecordUserName(uname)

if dbRecord:
  if uname == dbRecord["name"]:
    pwd = input('Enter the passwd: ')
    if inputEncrypPasswd(pwd) == dbRecord["passwd"]:
      print("LOGIN SUCCESS")
    else:
      print("password is invalid")
else:
  print("no username")
