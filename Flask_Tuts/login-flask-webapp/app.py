from flask import Flask , render_template , request


app = Flask(__name__)


@app.route("/")
def home():
  return render_template("home.html")

@app.route("/login")
def login():
  return render_template("LoginForm.html")


@app.route("/loginform",methods=["POST"])
def loginform():
  if request.method == "POST":
    print(request.form["Pass"], request.form["Uname"], request.form["email"])
    return "hello"

if __name__ == '__main__':
  app.run(port=1122,debug=True)