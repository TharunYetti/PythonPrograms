print("--------PERFECT NUMBERS BETWEEN THE RANGE---------")
n=int(input("Enter a number:"))
for i in range(1,n+1):
	add=0
	for j in range(1,i):
		if(i%j==0):
			add+=j
	if(add==i):
		print(i)
		
