# __init__.py # empty 

# Python Module example

def add(a, b):
   """This program adds two
   numbers and return the result"""

   result = a + b
   return f'Addition : {result}'


def sub(a, b):
   """This program adds two
   numbers and return the result"""

   result = a - b
   return f'Subtraction : {result}'

def mult(a,b):
	"""
	This program multiply two
   numbers and return the result

	"""

	result = a*b
	return f' Multiplication is {result}' 


def div(a,b):
	result= a/b
	return f'Division is : {result}'

def floor_div(a,b):
	result = a //b

	return f'Floor Division is : {result}'

def modulus(a,b):
	result = a % b

	return f'Modulus is : {result}'


def exponentaion(a,b):
	result = a ** b

	return f'Exponentaion is : {result}'


def greet():
	return f"Hey Hi ,Welcome to  Python Calci"