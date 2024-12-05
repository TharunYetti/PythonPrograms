num=int(input("Enter the No.of Elements do you want in the List: "))
L=[]
for i in range(0,num):
	element=int(input("Enter the List elements: "))
	L.append(element)
print("The List Created by the user is: ",L)
def list():	
	for j in L:
		if(L[0]==6 or L[-1]==6):
			return 1
		else:
			return 0				
x=list()
if(x==1):
	print("YES")
else:
	print("NO")	 	
	
