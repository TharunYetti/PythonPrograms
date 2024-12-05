print("Greatest number between two numbers")
num1=int(input('Enter a Number'))
num2=int(input('Enter another Number'))
if(num1<num2):
	print('{} is greater than {}'.format(num2,num1))
elif(num1>num2):
	print('{} is greater than {}'.format(num1,num2))
else:
	print('Both The Numbers are Equal')		
