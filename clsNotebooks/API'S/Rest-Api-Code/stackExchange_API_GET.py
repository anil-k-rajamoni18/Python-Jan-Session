import requests

import json

api_url = "https://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow"

response = requests.request("GET",url=api_url)

print(response.status_code) 

# print(response)

# print(response.json())

# print(response.json()["items"])

for question in response.json()["items"]:
  if(question["answer_count"]==0):
    print(question["title"])
    print(question["link"])
  else:
    print("Skipped....")