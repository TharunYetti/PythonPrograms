string=input('Enter a string:')
lower=0;upper=0;others=0
for letter in string:
	if(letter.islower()):
		lower+=1
	elif(letter.isupper()):
		upper+=1
	else:
		others+=1
print('No. of upper case letters in the string are {} an No.of Lower case letters in the string are {}'.format(upper,lower))
