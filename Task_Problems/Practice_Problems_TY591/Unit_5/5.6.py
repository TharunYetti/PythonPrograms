n=int(input("Enter how many lists do you want to enter:"))
li=[]
for i in range(n):
	n1=int(input("Enter how many elements do you want to enter in #{} lisr:".format(i+1)))
	k=[]
	for i in range(n1):
		k1=input("Enter element:")
		k.append(k1)
	li.append(k)
li.sort()
print(li)
