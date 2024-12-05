L=[]
while(True):
	print("\t\t\t****************\n a\t-to add an element\n p\t-to print the list\n v\t-find the average of the list of values\n r\t-to remove an element\n m\t-to find minimum of the list\n q\t-to quit")
	i=input("Enter your Choice: ")
	if(i=="a"):
		add=int(input("Enter the element to add into the list:"))
		L.append(add)
	elif(i=="p"):
		print(L)
	elif(i=="v"):
		if(len(L)==0):
			print("List should contain atleast one element.")
		else:
			avg=sum(L)/len(L)
			print("The average of the List is",avg)
	elif(i=="r"):
		if(len(L)==0):
			print("List should contain atleast one element.")
		else:
			rem=int(input("Enter the index value remove from list: "))
			if(rem>len(L) or rem<-len(L)):
				print('Index value should be valid')
			else:
				L.pop(rem)
	elif(i=="m"):
		if(len(L)==0):
			print("List should contain atleast one element.")
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
