char=input('Enter any Character: ')
if(char>='a' and char<='z' or char>='A' and char<='Z'):
	print('Given character',char,'is an Alphabet')
elif(char>='0' and char<='9'):
	print('Given Character',char,'is a digit')
else:
	print('Given Input is a special Character')
			
