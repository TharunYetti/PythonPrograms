n=int(input("Enter the no.of elements in the list: "))
L=[]
for i in range(n):
	e=int(input("Enter the Element in the list: "))
	L.append(e)
print(L)	
L.sort()
for i in L:
	c1=len(L)
	if(L.count(i)!=1):
		L.remove(i)
	print(L)					
