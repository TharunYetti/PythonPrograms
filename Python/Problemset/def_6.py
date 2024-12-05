def fact(a):
	for i in range(1,a+1,1):
		if(a%i==0):
			print(i)
num=int(input("Enter any Number: "))
fact(num)			
