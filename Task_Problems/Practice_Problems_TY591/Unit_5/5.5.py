k=input('ENter a line of strings')
spaces=0
letters=0
digits=0
for i in k:
	if(i.isspace()):
		spaces+=1
	elif(i.isdigit()):
		digits+=1
	elif(i.isalpha()):
		letters+=1
	else:
		print()
l=k.split()
print('No of words are',len(l))
print('No of letters are',letters)
print('No of digits are',digits)
print('No of spaces are',spaces)
		
