def minthree(num1,num2,num3):
	if(num1<num2 or num1<num3 ):
		print(num1,"is the Smallest Number")
	elif(num2<num3):
		print(num2,"is the smallest Number")	
	else:
		print(num3,"is the smallest Number")	
num1=int(input("Enter any Number: "))
num2=int(input("Enter the second Number: "))
num3=int(input("Enter the Third Number: "))
minthree(num1,num2,num3)
