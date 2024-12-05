print("Working place based on gender and age")
age=int(input('Enter Your Age: '))
sex=input('Enter Your Sex either (M/F): ')
marial_status=input('Have you Married or not say (Y/N): ')
if(sex=='F'):
	print('Then She will work only in Urban Areas')
elif(sex=='M' and 20<=age<40):
	print('He May Have to Work in Anywhere')
elif(sex=='M' and 40<=age<60):
	print('Then He will work only in Urban Areas')
else:
	print('You are not eligible for the job')
