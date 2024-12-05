import random
n=int(input("Enter any number to create a list with random numbers upto that number: "))
li=[]
for i in range(20):
	r=random.randrange(1,n+1)
	li.append(r)
li.sort()
print(li)
