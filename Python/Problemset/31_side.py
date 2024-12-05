side1=float(input('Enter the Length of side1: '))
side2=float(input('Enter the length of side2: '))
side3=float(input('Enter the length of side3: '))
if(side1+side2>side3 and side2+side3>side1 and side3+side1>side2):
	print('The given Lengths of sides can form the triangle')
else:
	print('The Given Lengths of sides do not form the Triangle')
		
