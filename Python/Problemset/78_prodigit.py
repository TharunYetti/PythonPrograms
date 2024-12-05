num=int(input("Enter any Number: "))
prod=1
while(num>0):
	c=num%10
	prod=prod*c
	num=num//10
print(prod)	
