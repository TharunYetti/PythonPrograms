password=input("Please Enter a Password: ")
while(True):
	if(len(password)<8):
		print("Password should be minimum 8 characters.")
	else:
		c=0;c1=0;c2=0;c3=0;c4=0;list=[]
		for i in password:
			if(password.count(i)>1):
				c+=1
				if(i not in list):
					list.append(i)	
			if(i.islower()==True):
				c1+=1
			elif(i.isupper()==True):
				c2+=1
			elif(i.isdigit()==True):
				c3+=1
			elif(i=="@" or i=="$" or i=="#" or i=="&"):
				c4+=1
			else:
				print("Given Password",password,"is not valid.\nPlease follow the primary condition for Password Validation")
	count_o=0
	if(c4==0):
		count_o+=1
		print("Given Password",password,"is not valid.\nPlease follow the primary condition for Password Validation")
	elif(c>=1):
		count_o+=1
		print("Given Password",password,"is not valid.\nFound Repeated Character(s) in the given string",end=":")
		print(*list,sep=",")
	elif(c1==0):
		count_o+=1
		print("Given Password",password,"is not valid.\nPlease follow the primary condition for Password Validation")
	elif(c2==0):
		count_o+=1
		print("Given Password",password,"is not valid.\nPlease follow the primary condition for Password Validation")
	elif(c3==0):
		count_o+=1
		print("Given Password",password,"is not valid.\nPlease follow the primary condition for Password Validation")
	if(count_o==0):
		print("Given Password",password,"is a strong Password and valid.\nThankYou")	
		break			 
	else:								
		password=input("Please Enter a Password again: ")
