def fact(a):
	for i in range (1,a+1,1):	
		if(a%i==0):
			print(i,end=",")
def factorial(b):
	fact=1
	for i in range(b,0,-1):
		fact=fact*i
	print(fact)	
num=int(input("Enter any Number: "))
fact(num)
factorial(num)		
		
