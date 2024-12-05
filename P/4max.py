n=int(input('ENter a number to find sum of even digits:'))
temp=n
evesum=0
oddsum=0
while(temp>0):
	dig=temp%10
	if(dig%2==0):
		evesum+=dig
	else:
		oddsum+=dig
	temp//=10
print('The sum of even digits of the number {} is {}'.format(n,evesum))
print('The sum of odd digits of the number {} is {}'.format(n,oddsum))


'''n1=int(input('Enter first number:'))
n2=int(input('Enter second number:'))
n3=int(input('Enter third number:'))
n4=int(input('Enter second number:'))
if(n1>=n2 and n1>=n3 and n1>=n4):
	print(n1,'is the Greatest Among the Four')
elif(n2>=n3 and n2>=n4):
	print(n2,'is the Greatest among the Four')
elif(n3>=n4):
	print(n3,'is the Greatest among the Four')
else:
	print(n4,'is the Greatest among the Four')'''


	


