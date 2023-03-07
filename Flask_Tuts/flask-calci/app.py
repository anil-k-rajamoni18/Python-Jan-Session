# importing 
from flask import Flask ,render_template,request


# create a object for Flask class
app = Flask(__name__)

# create a routes

@app.route("/")
def index():
  return render_template("home.html",data={"name":"kumar","course":"python","place":"hyd","fee":1092.289})

@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/greet/<name>")
def greet(name):
  return render_template("greet.html",username = name)


@app.route("/calci")
def calci():
  return render_template("cal.html")

@app.route("/calculation",methods=["GET","POST"])
def calculation():
  if request.method == "POST":
    print(request.form["num1"],request.form["num2"],request.form["op"])
    num1 = int(request.form["num1"])
    num2 = int(request.form["num2"])
    op = request.form["op"]

    result = 0
    if op=="+":
      result = num1+num2
    elif op=="-":
     result = num1-num2
    elif op=="*":
     result = num1*num2
    elif op=="/":
     result = num1/num2
    elif op=="%":
     result = num1%num2
     
    return render_template("result.html", data=f"{num1} {op} {num2} = {result}")

if __name__ == '__main__':
  app.run(debug=True,port=2211)
