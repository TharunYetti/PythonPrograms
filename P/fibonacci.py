n=int(input("Enter The Number upto which you have to print the fibonacci:"))
d=dict()
f1=0
f2=1
if(n<=0):
	print("The Number Should be Greater Than zero")
elif(n>=1):
	d[1]=f1
if(n>=2):
	d[2]=f2
i=3
while(i<=n):
	f3=f1+f2
	d[i]=f3
	f1=f2
	f2=f3
	i+=1
print(d,'is the Dictionary with Fibonacci Sequence:')
