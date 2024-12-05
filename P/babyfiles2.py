f=open('bank.txt','r+')
f.seek(0,0)
name=input('ENter Your Name to check your account:')
k=f.readline()
if(name.upper()==k.rstrip('\n')):
	print('YOUR ACOOUNT IS VERIFIED PROCEED!')
anum=int(input('ENTER YOUR ACCOUNT NUMBER TO PROCEED: '))
if(anum==int(f.readline())):
	print('USE THESE OPERATIONS TO HANDLE YOUR ACCOUNT'.center(149))
	while('Tharun'!='Topper'):
		f.seek(0,0)
		name_1=f.readline()
		ac_no=f.readline()
		balance=f.readline()
		k2=0
		for i in balance:
			if(i.isdigit()):
				k2=k2*10+int(i)			
		inp=input('ENTER,\tB-TO CHECK THE BALANCE IN YOUR ACCOUNT\n\tD- TO DEPOSIT IN YOUR ACCOUNT\n\tW- TO WITHDRAWL FROM YOUR ACCOUNT\n\tQ- TO QUIT THE OPERATIONS ===> Enter:')
		if(inp in 'bB'):
			print('======> Your Balance:',k2)
		elif(inp in 'dD'):
			f.seek(0,0)
			amount=int(input('======> Enter amount to deposit in account without any commas:'))
			if(amount<=0):
				print('Please Enter a valid amount!')
			else:
				k_rem=k2+amount	
				f.truncate(15)
				f.seek(0,2)
				f.write(str(k_rem))
				print('======> AMOUNT DEPOSITED SUCCESSFULLY!\n======> CHOOSE OPTION \'B\' TO CHECK THE BALANCE.')
		elif(inp in 'wW'):
			f.seek(0,0)
			amount=int(input('======> Enter amount to withdraw from yout account without any commas:'))
			if(amount>k2):
				print('======> There isn\'t that much enough amount in your account! Choose option \'B\' to check your current balance')
			else:
				k2_rem=k2-amount
				f.truncate(15)
				f.seek(0,2)
				f.write(str(k2_rem))
				print('======> PLEASE TAKE YOUR AMOUNT IN COLLECTION TAB\n======> CHOOSE OPTION \'B\' TO CHECK THE BALANCE ')
		elif(inp in 'qQ'):
			print('======> Thank You For Using Our Online Banking Services!')
			break
		else:
			print('======> You have choosen Invalid option\nPlease select valid option')
f.close()
