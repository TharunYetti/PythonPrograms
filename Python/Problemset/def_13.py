def factorial(a):
	first=1
	for i in range(a,0,-1):
		first=first*i
	print(first)
def first(a):
	while(a>0):
		dig=a%10
		a=a//10		
	factorial(dig)
num=int(input("Enter any Number: "))
first(num)			
