print("-----------FIBONACCI SERIES--------------")
n=int(input("Enter how many terms do you want in series:"))
a=0
b=1
if(n<=0):
	print('Please enter a positive range.')
elif(n==1):
	print(a)
else:
	print(a,b,sep=' ',end=' ')
	for i in range(2,n):
	    c=a+b
	    a=b
	    b=c
	    print(c,end=' ')
