num=int(input("Enter any Number: "))
num1=num
sum=0
while(num>0):
	dig=num%10
	cube=dig**3
	sum=sum+cube
	num=num//10
if(sum==num1):
	print(num1,"is an Armstrong Number")	
else:
	print(num1,"is not an armstrong number")	

	
