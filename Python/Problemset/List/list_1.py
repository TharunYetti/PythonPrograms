n=int(input("Enter the No.Of Elements in the list: "))
L=[]
for i in range(1,n+1):
	e=int(input("Enter the Elements in the List: "))
	L.append(e)
print("The List created by the user is:",L)
def list():
	new_List=[]
	for j in L:
		sum=0
		while(j>0):
			digit=j%10
			sum+=digit
			j=j//10
		new_List.append(sum)	
	print("The List With Sum of the Digits is :",new_List)
list()	
