from email.mime import application
from flask import Flask , render_template,request
from markupsafe import escape
import json
import requests

application = Flask(__name__) #instance of flask  #__name__ = __main__


@application.route("/")
def hello_world():
    return render_template('index.html')


@application.route('/convert',methods=["POST"])
def convert():
    if request.method=='POST':
        print("Hey HI")
        from1 = request.form["cnt1"]
        to = request.form["cnt2"]
        curr = request.form["sym"]

        url = "https://currency-converter13.p.rapidapi.com/convert"


        querystring = {"from":from1,"to":to,"amount":curr}

        headers = {
            'x-rapidapi-key': "bbc4e72c95msh764d7107571c9ccp132292jsne000b3620c23",
            'x-rapidapi-host': "currency-converter13.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        d=json.loads(response.text)
        res=f"{d['from']} to {d['to']} is {d['amount']}"

        return render_template('result.html',data=res)


if __name__=="__main__":
    application.run(debug=True, use_reloader=False)
