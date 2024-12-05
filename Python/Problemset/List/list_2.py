num=int(input("Enter the No.Of Elements in the List: "))
L=[]
for i in range(0,num):
	Element=int(input("Enter the Elements in the List"))
	L.append(Element)
print("The List defined by user is:",L)	
def factorial(a):
	factorial=1
	for i in range(a,0,-1):
		factorial=factorial*i
	return factorial
def lfactorial():
	new_List=[]
	for j in L:
		new_List.append(factorial(j))
	print("The List with the factorials is:",new_List)	
lfactorial()				
			
	
