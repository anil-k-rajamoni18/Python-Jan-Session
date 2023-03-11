import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user="root",
  password="root",
  port=3307,
  database='person'
)

print(mydb)

# create a cursor
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


mycursor.execute("SELECT * FROM user ")

myresult = mycursor.fetchall()

print(myresult)

for x in myresult:
  print(x)