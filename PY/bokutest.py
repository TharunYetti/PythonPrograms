n=int(input("number"))
z=n
d=0
if(n>0):
	x=n%10
while(n>0):
	z=n%10
	d=d*10+z
	n=n//10
if(d>0):
	y=d%10
print("First digit of the given number is {} and the last digit is {}".format(y,x))
