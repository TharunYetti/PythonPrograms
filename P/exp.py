pwd=input('Enter a Password:')
while(True):
	acount=0
	Acount=0
	dcount=0
	scount=0
	l=['@','$','#','&']
	l2=[]
	for i in pwd:
		if(i>='a' and i<='z'):
			acount+=1
		elif(i>='A' and i<='Z'):
			Acount+=1
		elif(i>='0' and i<='9'):
			dcount+=1
		elif(i in l):
			scount+=1
		if(pwd.count(i)>1):
			l2.append(i)
	stry=''
	for i in l2:
		if(i not in stry):
			stry+=i
	if(len(pwd)<8):
		print('Given Password {} is not valid.'.format(pwd))
		print('Please follow the Primary conditions for password validation')	
	elif(acount==0):
		print('Given Password {} is not valid.'.format(pwd))
		print('Please follow the Primary conditions for password validation')
	elif(Acount==0):
		print('Given Password {} is not valid.'.format(pwd))
		print('Please follow the Primary conditions for password validation')
	elif(dcount==0):
		print('Given Password {} is not valid.'.format(pwd))
		print('Please follow the Primary conditions for password validation')	
	elif(scount==0):
		print('Given Password {} is not valid.'.format(pwd))
		print('Please follow the Primary conditions for password validation')
	elif(len(stry)!=0):
		print('Given Password {} is not valid.'.format(pwd))
		print('Found repeted characters in given string:',end=' ')
		print(*stry,sep=',')
	else:
		print('Given password {} is Strong Password and Valid.'.format(pwd))
		print('Thank You')
		break
	pwd=input('Please enter strong password again:')
