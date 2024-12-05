def fact(num):
	for i in range(1,num+1):
		if(num%i==0):
			print(i,end=",")
def factorial(x):
	fact=1
	for i in range(x,0,-1):
		fact=fact*i
	print(fact,"\n")
def even(a,b):
	if(a%2==1):
		for i in range(a,b+1,2):
			fact(i)
			factorial(i)
	else:
		for i in range(a+1,b+1,2):
			fact(i)
			factorial(i)
start=int(input("Enter any starting Number: "))
end=int(input("Enter the ending Number: "))
even(start,end)
