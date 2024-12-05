l=[]
num=int(input("Enter the No.of elements do you ant in the list"))
for i in range(1,num+1):
	element=int(input("Enter the List Elemnt"))
	l.append(element)
print("The List is: ",l)
print("The Even Numbers are",end=":")
for i in l:
	if(i%2==0):
		print(i,end=",")	
