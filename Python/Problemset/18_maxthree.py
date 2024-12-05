num1=int(input('Enter the first number: '))
num2=int(input('Enter the second number: '))
num3=int(input('Enter the third Number: '))
if(num1==num2 and num2==num3 and num3==num1):
	print('All three Persons are of same age')
elif(num1>=num2 and num1>=num3):
	if(num1==num2):
		print('{} and {} are the Older Persons'.format('person1','person2'))
	elif(num1==num3):
		print('{} and {} are the Older Persons'.format('Person1','Person3'))
	else:
		print('{} is the Oldest Person'.format('Person1'))		
elif(num2>=num3):
	if(num3==num2):
		print('{} and {} are the Older Persons'.format('person2','person3'))
	elif(num1==num2):
		print('{} and {} are the Older Persons'.format('Person1','Person2'))
	else:
		print('{} is the Oldest Person'.format('Person2'))
else:
	if(num1==num3):
		print('{} and {} are the Older Persons'.format('person1','person3'))
	elif(num2==num3):
		print('{} and {} are the Older Persons'.format('Person2','Person3'))
	else:
		print('{} is the Oldest  Person'.format('Person3'))
	
