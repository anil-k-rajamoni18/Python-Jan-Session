import Calculator

while True:
  print("1.Addition\n2.Subtraction\n3.Multiplication\n -1. Exit")
  ch = int(input("Enter the choice: "))
  if(ch==1):
    print(Calculator.add())
  elif ch==2:
    print(Calculator.sub())
  elif ch==3:
    print(Calculator.multi())
  elif ch==-1:
    break
  else:
    print("provide valid choice")
