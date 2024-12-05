def digitsum(n):
	sum=0
	while(n>0):
		digit=n%10
		sum+=digit
		n//=10
	print("The sum of digits is",sum)
n=int(input("ENter a number:"))
digitsum(n)
