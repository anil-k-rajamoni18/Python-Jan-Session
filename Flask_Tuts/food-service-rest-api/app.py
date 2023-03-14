from flask import Flask,request
from DB.MongoUtils import *
import json
from bson import json_util

app = Flask(__name__)

collObj = None

def createDBConnection():
  global collObj
  collObj = CreateConnection()

@app.route("/")
def index():
  return "Greetings from food rest mirco service is up and running..."

@app.route("/api/food",methods=["GET"]) #to get one food item
def getFoodItem():
  apiResponseData = findOneRecord(collObj)
  print(apiResponseData)
  return apiResponseData


@app.route("/api/fooditems",methods=["GET"]) #to get list of all food items.
def getFoodItems():
  apiResponseData = findAllRecords(collObj)
  return apiResponseData

@app.route("/api/food",methods=["POST"])
def saveFoodItem():
  if request.method == "POST":
    data = request.get_json()
    return insertOne(collObj,data)


@app.route("/api/fooditems",methods=["POST"])
def saveFoodItems():
  if request.method == "POST":
    data = request.get_json()
    return insertMany(collObj,data)






if __name__ == '__main__':
  createDBConnection()
  app.run(port = 2211,debug = True)