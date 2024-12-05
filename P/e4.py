L=[]
while(True):
	print("\t\t\t****************\n a\t-to add an element\n p\t-to print the list\n v\t-find the average of the list of values\n r\t-to remove an element\n m\t-to find minimum of the list\n q\t-to quit")
	Sum=0
	Len=0
	for i in L:
		Sum+=i
		Len+=1
	i=input("Enter your Choice: ")
	if(i=="a"):
		add=int(input("Enter the element to add into the list:"))
		L.append(add)
	elif(i=="p"):
		print(L)
	elif(i=="v"):
		if(Len==0):
			print("List should contain atleast one element.")
		else:
			avg=Sum/Len
			print("The average of the List is",avg)
	elif(i=="r"):
		if(Len==0):
			print("List should contain atleast one element.")
		else:
			rem=int(input("ENter the index value remove from list: "))
			if(rem in range(Len)):
				L.remove(L[rem])
			else:
				print("You should enter a valid range.")
	elif(i=="m"):
		if(Len==0):
			print("list should contain atleast one element.")
		else:
			mini=L[0]
			for i in L:
				if(i<mini):
					mini=i
			print("Minimum of the List is",mini)
	elif(i=="q"):
		print("End of the Program.")
		break
	else:
		print("Please enter a valid input.")

