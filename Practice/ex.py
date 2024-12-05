def factorial():
	a=int(input("Enter any Positive Number to find its factorial: "))
	fact=1
	for i in range(a,0,-1):
		fact=fact*i
	print("Factorial of a Given Number {} is: {}".format(a,fact))
def even():
	b=int(input("Enter any Positive Number to print even digits of a Number: "))
	print("Even digits of a given number are",end=":")
	while(b>0):	
		dig=b%10
		if(dig%2==0):
			print(dig,end=",")
		b=b//10
	print()	
def prime():
	num=int(input('Enter any Positive Number to find whether it is prime or not: '))
	i=1
	c=0
	while(i<=num):
		if(num%i==0):
			c=c+1
		i+=1
	if(c==2):
		print('Entered Number is a prime number')
	else:
		print('Entered Number is not a prime number')	
n=0								
while(n<=0):
	num=int(input("Enter a Number among 1,2,3 and 0: "))
	if(num==1):
		factorial()
	elif(num==2):
		even()
	elif(num==3):
		prime()
	elif(num==0):
		print("Good Bye!!!")
		break			
	else:
		print("Enter Valid Input and try again")
	n+=0
		
                                                                        
