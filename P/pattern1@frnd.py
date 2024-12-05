n=int(input("\nEnter no.of rows you want:"))
for i in range(1,n+1):
	k=i
	print("  "*(n+1-i),end="\b") #use double space here mowa
	for j in range(1,i+1):
		print(k,end=" ")
		k+=1
	for l in range(1,i):
		print(k-2,end=" ")
		k-=1
	print()	
print("\nMowa intha chesinanduku repu biryani order pettu ra!\n")
