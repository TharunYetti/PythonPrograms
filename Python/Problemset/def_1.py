def divisible(a,b):
	for i in range(a,b+1,1):
		if(i%3==0 and i%12==0):
			print(i)
a=int(input("Enter the Starting Number: "))
b=int(input("Enter the Ending Number: "))			
divisible(a,b)			

	
