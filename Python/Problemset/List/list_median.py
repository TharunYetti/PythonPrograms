num=int(input("Enter the No.of Elements in the list: "))
L=[]
for i in range(1,num+1):
	element=int(input("Enter the List element: "))
	L.append(element)
L.sort()
print(L)
def median():
	m1=int(num/2)
	m2=int((num-1)/2)
	if(num%2!=0):
		print(L[m1])
	else:	
		print(L[m1])
		print(L[m2])		
print("The Median(s) of the Elements in the is:");median()			
