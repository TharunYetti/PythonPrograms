num=int(input('Enter:'))
while(num%2==0):
	while(num%4==0):
		while(num%8==0):
			print('DIVISIBLE')
			break
		else:
			print('NOT DIVISIBLE BY 8')
		break
	else:
		print('NOT DIVISIBLE BY 4 and 8')
	break
else:
	print('NOT DIVISIBLE BY 2,4 and 8')
																			


