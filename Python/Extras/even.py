start=int(input("Enter Starting Value: "))
end=int(input("Enter Ending Value: "))
even=str()
if(start%2==0):
	for i in range(start,end+1,2):
		if(i==end or i==end-1):
			i=str(i)
		else:
			i=str(i)+str(",")	
		even=str(even)+str(i)
	print("The Even Numbers are:",even)	
else:
	for i in range(start+1,end+1,2):
		if(i==end or i==end-1):
			i=str(i)
		else:
			i=str(i)+str(",")	
		even=str(even)+str(i)
	print("The Even Numbers are:",even)	
		

	
