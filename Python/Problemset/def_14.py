def prime(a):
	c=0
	for i in range(1,a+1):
		if(a%i==0):
			c+=1
	if(c==2):
		print(i)		
def num(a,b):
	for i in range(a,b+1,1):
		prime(i)
start=int(input("Enter the starting Number: "))
end=int(input("Enter the Ending Number: "))
num(start,end)		
		
