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

@app.route("/api/fooditems",methods=["GET"])
def getFoodItems():
  ResponseData = findOneRecord(collObj)
  responseResult = []
  if ResponseData:
    for data in ResponseData:
      responseResult.append({data:ResponseData[data]})

  responseResult = {"data": responseResult}
  print(responseResult)
  return responseResult

@app.route("/api/food/",methods=["POST"])
def saveFoodItem():
  if request.method == "POST":
    print(request.get_json())









if __name__ == '__main__':
  createDBConnection()
  app.run(port = 2211,debug = True)