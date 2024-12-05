def reverse(n):
	rev=0
	while(n>0):
		digit=n%10
		rev=rev*10+digit
		n//=10
	print("The reverse Number is",rev)
n=int(input("Enter a number:"))
reverse(n)
