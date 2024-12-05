start=int(input("Enter the Starting Number: "))
end=int(input("Enter the Ending Number: "))
even=str()
for i in range(start,end+1):
	if(i%2==0):
		if(i==end or i==end-1):
			i=str(i)
		else:
			i=str(i)+","
		even=even+i
print("The Even Numbers are:",even)				
