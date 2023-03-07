# step 1: import the Flask class
from flask import Flask , render_template

# step2: obj for Flask class

app = Flask(__name__) #__main__



userData=[{"name":"Kumar","role":"SDE"},
{"name":"Lavanya","role":"PythonDev"},
{"name":"Rafal","role":"Full Stack Dev"}]

# create the routes 

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/home")
def home():
  from datetime import datetime
  today = datetime.now()
  return render_template("home.html",response=f"Hello welcome to home page {today}")


@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/about")
def about():
  return render_template("aboutus.html",data=userData)

@app.route("/user/<name>")
def userpage(name):
  return render_template("userpage.html",data=name)


if __name__ == '__main__':
  app.run(debug=True) #port : 5000
