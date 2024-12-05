year=int(input('Enter any year: '))
if(year%100!=0):
	if(year%4==0):
		print(year,"Is a Leap year")
elif(year%100==0 and year%4==0 and year%400==0):
	print(year,"Is a Leap year")
else:
	print(year,"is a non-leap year")				
