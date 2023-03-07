# importing 
from flask import Flask ,render_template


# create a object for Flask class
app = Flask(__name__)

# create a routes

@app.route("/")
def index():
  return render_template("home.html",data={"name":"kumar","course":"python","place":"hyd","fee":1092.289})

@app.route("/login")
def login():
  return render_template("login.html")


if __name__ == '__main__':
  app.run(debug=True,port=2211)
