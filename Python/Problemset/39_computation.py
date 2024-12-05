hour=int(input("Enter the Total Number of Hours worked: "))
rate=int(input("Enter the Rate: "))
if(hour>40):
	print("The Amount To be Paid is:",40*rate+(hour-40)*rate*1.5)
else:
	print('The Amount tom be Paid is:',hour*rate)	 
