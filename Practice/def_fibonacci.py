def fibonacci(num):
	n1=0
	n2=1
	for i in range(1,num+1,1):	
		print(n1)
		next=n1+n2
		n1=n2
		n2=next
num=int(input("Enter any Number: "))
fibonacci(num)		
