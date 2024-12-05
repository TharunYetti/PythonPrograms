def sdivi(a,b):
	sum=0
	for i in range(a,b+1,1):
		if(i%3==0 and i%12==0):
			sum=sum+i
	print(sum)	
a=int(input("Enter the Starting Number: "))
b=int(input("Enter the Ending Number: "))			
sdivi(a,b)	
