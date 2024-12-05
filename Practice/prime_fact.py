num=int(input("Enter any Number: "))
for i in range(1,num+1):
	if(num%i==0):
		c=0
		for j in range(1,i+1):
			if(i%j==0):
				c+=1
		if(c==2):
			print(i)
