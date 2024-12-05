num=int(input("Enter any Number:"))
num1=num
sum=0
while(num>0):
	dig=num%10
	fact=1
	while(dig>0):
		fact=fact*dig
		dig=dig-1
	sum=sum+fact	
	num=num//10
if(sum==num1):
	print(num1,"is a strong Number")
else:
	print(num1,"is not a strong Number")			
		
		
