print('''+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=CONDITIONS=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\nPrimary conditions for password validation:\n1.Password should be minimum 8 characters.\n2.In password, should not be repeated any character [either alphabet, number, special character]\n3.The password should contain at least 1 alphabet in lowercase [a-z].\n4.The password should contain at least 1 alphabet in uppercase [A-Z].\n5.The password should contain at least 1 digit [0-9].\n6.The password should contain at least 1 special character among these four only [@, $, #, &].\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=CONDITIONS=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+''')
pwd=input('Enter a Password:')
while(True):
	acount=0;Acount=0;dcount=0;scount=0;otherchr=0
	l=['@','$','#','&'];l1=[]
	for i in pwd:
		if(pwd.count(i)>1):
			l1.append(i)
		if(i>='a' and i<='z'):
			acount+=1
		elif(i>='A' and i<='Z'):
			Acount+=1
		elif(i>='0' and i<='9'):
			dcount+=1
		elif(i in l):
			scount+=1
		else:
			otherchr+=1	
	stry1=''
	for i in l1:
		if(i not in stry1):stry1+=i
	if(otherchr!=0):
		print('Given Password {} is not valid.'.format(pwd),'\nPlease follow the Primary conditions for password validation')
	elif(len(pwd)<8):
		print('Given Password {} is not valid.'.format(pwd),'\nPlease follow the Primary conditions for password validation')	
	elif(acount==0):
		print('Given Password {} is not valid.'.format(pwd),'\nPlease follow the Primary conditions for password validation')
	elif(Acount==0):
		print('Given Password {} is not valid.'.format(pwd),'\nPlease follow the Primary conditions for password validation')
	elif(scount==0):
		print('Given Password {} is not valid.'.format(pwd),'\nPlease follow the Primary conditions for password validation')
	elif(len(stry1)!=0):
		print('Given Password {} is not valid.'.format(pwd),'\nFound repeted characters in given string:',end=' ')
		print(*stry1,sep=',')
	elif(dcount==0):
		print('Given Password {} is not valid.'.format(pwd),'\nPlease follow the Primary conditions for password validation')
	else:
		print('Given password {} is Strong Password and Valid.'.format(pwd),'\nThank You')
		break
	pwd=input('Please enter strong password again:')
