def prime(a):
	c=0
	for i in range(1,a+1,1):
		if(a%i==0):
			c+=1
	if(c==2):
		print("It is a Prime Number")
	else:
		print("It is not a prime Number")
num=int(input("Enter any Number: "))
prime(num)					
prime(11)
prime(12)
prime(13)
prime(14)
prime(15)
			
