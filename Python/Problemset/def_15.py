def fact(a):
	for i in range(1,a+1):
		if(a%i==0):
			print(i)
def digit(x):
	while(x>0):
		digit=x%10
		fact(digit)
		x=x//10
num=int(input("Enter any Number: "))
digit(num)					
			
