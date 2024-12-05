n=int(input("Enter a number:"))
sum=0
while(n>0):
	dig=n%10
	sum+=dig
	n//=10
print("The sum of digits in {} is {}".format(n,sum))
