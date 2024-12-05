def maxmin(n):
	L=[]
	for i in  range(1,n+1):
		elements=int(input("Enter the List Elements: "))
		L.append(elements)
	print("The List created is: ",L)
	print("The Maximum Value in the List is: ",max(L))
	print("The Minimum Value in the list is: ",min(L))
n=int(input("Enter the No.of List Elements: "))
maxmin(n)

	
