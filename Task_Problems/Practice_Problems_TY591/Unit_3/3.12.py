print("---------STRONG NUMBER------------")
n=int(input('Enter A number:'))
for i in range(1,n+1):
	k=i
	sum=0
	while(i>0):
    		digit=i%10
    		fact=1
    		for j in range(digit,0,-1):
       			fact=fact*j
    		sum=sum+fact
    		i//=10
	if(sum==k):
    		print(k,end=" ")
