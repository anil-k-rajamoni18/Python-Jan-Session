from flask import Flask, render_template 

import json
import requests


app = Flask(__name__)


def get_meme():
  # src = "wholesomememes"
  # url = "https://meme-api.herokuapp.com/gimme" + src

  url = "https://meme-api.com/gimme/wholesomememes/1"

  response = requests.request("GET", url)
  print(response.status_code)

  if(response.status_code==200):
    data = response.json()
    meme_large = data["memes"][0]["preview"][-1]

    subreddit = data["memes"][0]["title"]

    return meme_large, subreddit


@app.route("/")
def home():
  return "<h2> Hello Welcome to Memes Page </h2>"

@app.route("/meme")
def getmeme():
  meme_pic, title = get_meme()

  print(meme_pic, title)

  return render_template("meme_index.html",meme_pic = meme_pic , title = title) 



if __name__ == '__main__':
  app.run(host='0.0.0.0',port=1122,debug=True)

  