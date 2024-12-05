p1=int(input("Enter the age of person1: "))
p2=int(input("Enter the age of person2: "))
p3=int(input("enter the age of Person3: "))
if(p1>=p2 and p1>=p3):
	if(p1==p2 and p1==p3):
		print('p1 p2 and p3 are of same age')
	elif(p1==p2):
		print('p1 and p2 are Older Persons')
	elif(p1==p3):
		print('p1 and p3 are Older Persons')
		
	else:
		print('P1 is the Oldest person')		
elif(p2>=p3):
	if(p2==p3):
		print('p2 and p3 are The Oldest Persons')
	else:
		print('p2 is the Oldest Person')	
elif(p3>=p2):
	if(p3==p2):
		print('p3 and p2 are older persons')
	else:	
		print(p3,"is the Oldest Person")
if(p1<=p2 and p1<=p3):
	if(p1==p2 and p1==p3):
		print('p1 p2 and p3 are of same age') 
	elif(p1==p2):
		print('p1 and p2 are Younger Persons')
	elif(p1==p3):
		print('p1 and p3 are Younger Persons')
	else:
		print('P1 is the Youngest person')
elif(p2<=p3):
	if(p2==p3):
		print('p2 and p3 are the Younger persons')
	else:
		print(p2,"is the Youngest person")
elif(p3<=p2):
	if(p3==p2):
		print('p2 and p3 are Younger Persons')
	else:	
		print(p3,"Is the Youngest Person")
else:
	print('p1 p2 p3 are of same age')							
