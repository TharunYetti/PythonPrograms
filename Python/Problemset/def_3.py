def maxthree(num1,num2,num3):
	if(num1>num2 and num1>num3 ):
		print(num1,"is the greatest Number")
	elif(num2>num3):
		print(num2,"is the greatest Number")	
	else:
		print(num3,"is the Greatest Number")	
num1=int(input("Enter any Number: "))
num2=int(input("Enter the second Number: "))
num3=int(input("Enter the Third Number: "))
maxthree(num1,num2,num3)			
