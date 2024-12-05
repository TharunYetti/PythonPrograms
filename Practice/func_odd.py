def oddadd(a):
	sum=0
	for i in range(1,a+1,2):
		sum+=i
	print(sum)
num=int(input("Enter any Number: "))
oddadd(num)		
