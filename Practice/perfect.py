'''num=int(input("Enter any Number: "))
i=1
sum=0
while(i<num):
	if(num%i==0):
		sum=sum+i
	i+=1
if(sum==num):
	print(num,"is a Perfect Number")
else:
	print(num,"is not a Perfect Number")'''
num=int(input("Enter any Number: "))
sum=0
for i in range(1,num):
	if(num%i==0):
		sum+=i
if(sum==num):
	print(num,"is a perfect Number")
else:
	print(num,"is not a perfect Number")							
	
	


