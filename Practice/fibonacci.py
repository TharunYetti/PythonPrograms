num=int(input("Enter any Number:"))
for i in range(1,num+1):
	s1=0
	s2=1
	for j in range(1,i+1):
		print(s1)
		s2=s2+s1
		s1=s1+s2
