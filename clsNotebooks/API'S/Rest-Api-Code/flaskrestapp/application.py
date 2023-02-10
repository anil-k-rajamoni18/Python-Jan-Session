from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.sqlite3"
    db.init_app(app)

    # with app.app_context():
    #     db.create_all()
    #     db.session.add(Drink(name="Mango",description="Tastes like Mango"))
    #     db.session.add(Drink(name="PineApple",description="Tastes like Sweety"))
    #     db.session.commit()
    #     print("DB created...")

    return app

class Drink(db.Model):
  id = db.Column(db.Integer , primary_key=True)

  name = db.Column(db.String(80),unique=True,nullable = False)

  description = db.Column(db.String(120))

  def __repr__(self):
    return f"{self.name} - {self.description}"

app = create_app()

@app.route("/")
def index():
  return 'Greetings from drink api , UP AND RUNNING ....!'

@app.route("/drinks")
def getDrinks():
  drinks = Drink.query.all()
  output = []
  for drink in drinks:
    drink_data = {'name': drink.name , "description" : drink.description}
    output.append(drink_data)

  return {"drinks": output}


@app.route("/drinks/<id>")
def getDrink(id):
  drink = Drink.query.get_or_404(id)
  return {"name":drink.name , "description": drink.description}


@app.route("/drinks",methods=["POST"])
def add_drink():
 if request.method == "POST":
    drink = Drink(name=request.json["name"],description=request.json["description"])
    db.session.add(drink)
    db.session.commit()
    return {"id":drink.id}

if __name__ == '__main__':
  app.run(host='0.0.0.0' , port = 1122, debug= True)
