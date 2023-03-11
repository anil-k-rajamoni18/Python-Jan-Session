from flask import Flask , render_template , request
from DB.MongoUtils import *
from DB.CommonUtils import encrypt


app = Flask(__name__)
collObj = None

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/login")
def login():
  return render_template("LoginForm.html")


def createDBConnection():
  global collObj
  collObj = CreateConnection()

@app.route("/loginform",methods=["POST"])
def loginform():
  if request.method == "POST":

    username = request.form["Uname"]
    passwd = request.form["Pass"]
    email = request.form["email"]
    msg = ""
    print(username , passwd , email)
    response_Data = findByUserName(collObj,username)
    print(response_Data)
    if response_Data:
      if response_Data["username"] == username:
        if response_Data["password"] == encrypt(passwd):
          msg = "LOGIN SUCCESS"
        else:
          msg = "INVALID PASSWORD...."
      else:
        msg = "INVALID USERNAME..."
        
    else:
      msg = "NO MATCHING RECORD WITH USERNAME...."

    return render_template("response.html",msg = msg)

if __name__ == '__main__':
  createDBConnection()
  app.run(port=1122,debug=True)
  