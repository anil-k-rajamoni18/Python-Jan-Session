from flask import Flask,render_template

# create a obj 
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html",name="Python Session On Flask")

@app.route("/<name>")
def greet(name):
  return f"<h1><center> Hey Hi Hello , Welcome {name}</center></h1>"

if __name__ == '__main__':
  app.run(debug=True)