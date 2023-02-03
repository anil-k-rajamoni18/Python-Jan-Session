import time

def greet(name):
  return f"Hey hi {name}"

def todayTime():
  return f'''today is {time.strftime("%Y-%m-%d:%H.%M.%S")}'''


def add(a,b):
  print(a+b)