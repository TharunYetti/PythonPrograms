print("Allowance to exam hall with  medical probelm")
class_held=int(input('Enter the No.of Days Classes Held: '))
class_attend=int(input('No.of Days you attended the class: '))
attend=(class_attend*100)/class_held
med=input('Do You Have Any Medical Cause?Say (y/n)....')
if(attend>=75):
	print('You are allowed to enter into the exam hall')
elif(attend<75 and med=='y'):
	print('You are allowed into the ExamHall')
else:
	print('You are Not Allowed into the ExamHall.!') 	
	
