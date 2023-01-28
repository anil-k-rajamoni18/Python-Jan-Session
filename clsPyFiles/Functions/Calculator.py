def add():
    '''This code handles the addition of integers and float values..by @raviteja'''
    num1 = int(input("Enter the num1: "))
    num2 = int(input("Enter the num2: "))
    if type(num1) in [int,float] and type(num2) in [int,float]:
        return  f'The addition of {num1} + {num2} is {num1+num2}'
    else:
        return "Not Valid Input"

def sub():
    '''This code handles the difference of integers and float values..by @raviteja'''
    num1 = int(input("Enter the num1: "))
    num2 = int(input("Enter the num2: "))
    if type(num1) in [int,float] and type(num2) in [int,float]:
        return f'The difference of {num1} - {num2} is {num1-num2}'
    else:
        return"Not Valid Input"

def multi():
    '''This code handles the multiplication of integers and float values..by @raviteja'''
    num1 = int(input("Enter the num1: "))
    num2 = int(input("Enter the num2: "))
    if type(num1) in [int,float] and type(num2) in [int,float]:
        return f'The addition of {num1} * {num2} is {num1*num2}'
    else:
        return "Not Valid Input"

def divide(num1,num2):
    '''This code handles the division of integers and float values..by @raviteja'''
    if type(num1) in [int,float] and type(num2) in [int,float]:
        return f'The division of {num1} / {num2} is {num1/num2}'
    else:
        return("Not Valid Input")


# print(divide(10,20))
