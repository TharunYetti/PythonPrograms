print("Grades of a student by taking marks")
marks=int(input('Enter your Marks '))
if(marks<25):
	print('Corresponding grade for your marks is:F')
elif(25<=marks<45):
	print('Corresponding grades for Your Marks is:E')
elif(45<=marks<50):
	print('The Corresponding Grade for Your Marks is:D')
elif(50<=marks<60):
	print('The Corresponding Grade for your marks is:C')
elif(60<=marks<80):
	print('The Corresponding Grade for your Marks is:B')
elif(marks>=80):
	print('The Corresponding Grade for your Marks is:A')						 
