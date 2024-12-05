print("Oldest and Youngest among three")
person1=int(input('Enter the Age of Person1 '))
person2=int(input('Enter the age of Person2 '))
person3=int(input('Enter the age of Person3 '))
if(person1>person2 and person1>person3):
	print('Person1 is the oldest person')
elif(person2>person1 and person2>person3):
	print('Person2 is the oldest person')
elif(person3>person1 and person3>person2):
	print('Person3 is the Oldest Person')
else:
	print('All are at the same Age')
if(person1<person2 and person1<person3):	
	print('Person1 is the Youngest person')
elif(person2<person1 and person2<person3):
	print('Person2 is the Youngest Person')
elif(perzon3<person1 and person3<person2):
	print('Person3 is the youngest person')
else:
	print('All are at the same Age')						  
