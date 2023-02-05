def factorial(num)->str:
  fact = 1
  for i in range(1,num+1):
    fact = fact*1
  return f"the factorial is {fact}"


def greet(name):
  print(f"Hey hi Welcom {name}")

def maxOfList(lst)->int:
  print(f"max of listElements is {max(lst)}")


def addition(num1,num2)->int:
  c = num1+num2
  return c