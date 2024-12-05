print("Bonus amount for an employee")
salary=int(input('Enter your monthly salary'))
service=int(input('Enter your no.of years of service'))
bonus=(5*salary)/100
if(service>5):
	print('Your Bonus Amount is:',bonus)
else:
	print('No bonus amount for you')	
