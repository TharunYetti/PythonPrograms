def factorial(a):
	fact=1
	for i in range(a,0,-1):
		fact=fact*i
	print(fact)
num=int(input("Enter any Number: "))
factorial(num)		
