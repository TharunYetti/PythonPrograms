n=int(input("Enter n:"))
l1=list()
for i in range(n):
	l1.append(input())
m=0
for i in l1:
	if len(i)>m:
		m=len(i)
k=0
for i in range(m):
	for i in l1:
		if(k<len(i)):
			print(i[len(i)-1-k],end="")
	k=k+1
print()
