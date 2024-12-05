def ifact(a,b):
	for i in range(a,b+1,1):
		for j in range(1,i+1):
			if(i%j==0):
				print(j)
		print()	
a=int(input("Enter any Number: "))
b=int(input("Enter the Ending number: "))
ifact(a,b)			
