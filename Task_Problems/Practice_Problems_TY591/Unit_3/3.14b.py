n=int(input("Enter a number:"))
for i in range(1,n):
	for j in range(i):
		print("*",end=" ")
	print()
for k in range(n,0,-1):
	for m in range(k):
		print("*",end=" ")
	print()
