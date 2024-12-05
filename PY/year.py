num=int(input("Enter the year:"))
four=num%4
hundred=num%100
fhundred=num%400
if(num%100!=0):
	if(num%4==0):
		print("It is a leap year")
elif(num%100==0 and num%4==0 and num%400==0):
	print("it is a leap Year")
else:
	print("It is a non leap year")	

			
