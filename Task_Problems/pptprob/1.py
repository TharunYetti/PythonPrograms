def recur(n):
	if(n<=1):
		return n
	else:
		return(recur(n-1)+recur(n-2))
num=int(input("Enter How many terms do you want:"))
if(num<=0):
	print('ENTER A VALID POSITIVE NUMBER!!!!!!!!!!')
else:
	for i in range(num):
		print(recur(i))
