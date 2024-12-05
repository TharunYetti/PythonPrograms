num=int(input("Enter any Number: "))
i=1
sum=0
while(i<num):
	if(num%i==0):
		j=1
		c=0
		while(j<=i):
			if(i%j==0):
				c+=1
			j+=1	
		if(c==2):
			sum=sum+i					
	i+=1	
print(sum)			
