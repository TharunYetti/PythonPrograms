num=int(input('Enter any Number: '))
five=num%5
eleven=num%11
if(five==0):
	print('{} is Divisible by Five'.format(num))
else:
	print('{} is Not Divisible by Five'.format(num))
if(eleven==0):
	print('{} is Divisible by Eleven'.format(num))
else:
	print('{} is Not Divisible by Eleven'.format(num))
				
