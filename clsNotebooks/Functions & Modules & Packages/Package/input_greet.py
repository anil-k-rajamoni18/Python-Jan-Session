from Package import calculator

# from Package.calculator import *



while True:
	print("""

	1.Addition
	2.Subtraction
	3.Multiplication
	4.Division
	5.Floor Division
	6.Modulus
	7.Expo
	8.exit
		""")
	user_input = int(input("Enter the Choice :"))
	if user_input == 8:
		break

	a = int(input("Enter num1 "))

	b = int(input("Enter num2 "))

	if user_input ==1:
		print(calculator.add(a,b))


	elif user_input ==2:
		print(calculator.sub(a,b))


	elif user_input ==3:
		print(calculator.mult(a,b))


	elif user_input ==4:
		print(calculator.div(a,b))


	elif user_input ==5:
		print(calculator.floor_div(a,b))


	elif user_input ==6:
		print(calculator.modulus(a,b))

	elif user_input ==7:
		print(calculator.exponentaion(a,b))


	else:
		print("Invalid Choice ...")

 
 


