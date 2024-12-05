print("---------WELCOME TO SIMPLE CALACULATOR---------")
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
print("PLEASE SELECT YOUR OPERATION\n1:ADDITION\n2:SUBTRACTION\n3:PRODUCT\n4:DIVISON\n5:FLOOR DIVISION\n6:REMAINDER\n7:POWER")
c=int(input("Now enter the operation: "))
if(c==1):
	print("Adiition of num1 and num2 is",a+b)
elif(c==2):	
	print("Subtraction of num2 from num1 is",a-b)
elif(c==3):
	print("product of num1 and num2 is",a*b)
elif(c==4):
	print("Division of num1 by num2 is",a/b)
elif(c==5):
	print("Floor division of num1 by num2 is",a//b)
elif(c==6):
	print("Remainder of the divison of num1 by num2 is",a%b)
elif(c==7):
	print("Power of num2 to num1 is",a**b)
else:
	print("Please Enter valid operation")
print("--------THANK YOU-------")
