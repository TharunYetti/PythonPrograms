def fact(b):
	for i in range(1,b+1):
		if(b%i==0):
			print(i)
def first(a):
	while(a>0):
		dig=a%10
		a=a//10		
	fact(dig)
num=int(input("Enter any Number: "))
first(num)

					
