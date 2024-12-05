def primeornot(k):
	fact=0
	for i in range(1,k+1):
		if(k%i==0):
			fact+=1
	if(fact==2):
		print("It is a Prime Number.")
	else:
		print("It is not a Prime Number.")
k=int(input("Enter a number:"))
primeornot(k)
