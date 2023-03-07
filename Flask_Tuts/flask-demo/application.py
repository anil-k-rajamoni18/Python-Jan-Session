from flask import Flask , render_template , request

# create a flask obj 

app = Flask(__name__)

# create routes 

@app.route("/")
def home():
  return "HOME PAGE...."


@app.route("/greet")
def login():
  return "Hey Hi Welcome to my Website"


@app.route("/greet/<name>")
def greet(name):
  return render_template("home.html",data = f"Hey Hi Welcome {name}")

@app.route("/cal")
def cal():
  return render_template("calculator.html")


@app.route("/calci",methods=["GET","POST"])
def calci():
  if request.method == "POST":
    num1 = int(request.form["num1"])
    num2 = int(request.form["num2"])
    symbol = request.form["symbol"]
    result = 0;
    if symbol == "+":
      result = num1+num2
    elif symbol == "-":
      result = num1-num2
    elif symbol == "*":
      result = num1*num2
    elif symbol == "/":
      result = num1/num2
    else:
      result = -1

  return f"operation of {symbol} on {num1} and {num2}  == {result} "




if __name__ == '__main__':
  app.run(debug=True)