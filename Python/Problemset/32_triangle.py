side1=float(input('Enter the length of side1: '))
side2=float(input('Enter the length of side2: '))
side3=float(input('Enter the length of side3: '))
if(side1==side2==side3):
	print('The Triangle formed is an Equilateral Triangle')
elif(side1==side2 or side2==side3 or side3==side1):
	print('The Triangle formed is an Isosceles Triangle')
else:
	print('The Triangle formed is a Scalen Triangle')		
