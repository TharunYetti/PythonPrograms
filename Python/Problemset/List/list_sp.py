n=int(input("Enter the No.of List Elements: "))
L=[]
for i in  range(1,n+1):
	elements=int(input("Enter the List Elements: "))
	L.append(elements)
print("The List created is: ",L)
def list():
	s=0
	prod=1
	for j in L:
		s=s+j		
		prod=prod*j
	print(s,"is the sum of the elements in the list")
	print(prod,'is the product of the elements in the list')
list()			
