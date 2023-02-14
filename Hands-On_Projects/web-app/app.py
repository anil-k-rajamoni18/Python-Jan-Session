from flask import Flask,render_template,request

# create a obj 
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html",name="Python Session On Flask")

@app.route("/<name>")
def greet(name):
  return f"<h1><center> Hey Hi Hello , Welcome {name}</center></h1>"

@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/retrive",methods=["GET","POST"])
def retrive():
  if request.method== "POST":
    print(request.form["fname"])
    print(request.form["passwd"])
    
  return "Successfully data stored..."
if __name__ == '__main__':
  app.run(debug=True)