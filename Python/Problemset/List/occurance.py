L=[1,2,3,4,5,1,2,3,5,7,8,6,9]
max=max(L)
min=min(L)
for i in range(min,max+1):
	k=L.count(i)
	for j in range(1,len(L)):
		if(j==k):
			print(i,j)
	L.remove(i)
L.sort()		
print(L)		
	
