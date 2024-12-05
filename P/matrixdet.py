print('+=+=+=+=+=+=+=+=+=+= Matrix determinant =+=+=+=+=+=+=+=+=+=+='.center(148))
n=int(input('Enter the order of square matrix among 1,2 and 3 to find its determinant:'))
if(n==0):
	print('A matrix should contain atleast one element!')

elif(n==1):
	ele=int(input('Enter element a11:'))
	print('the dterminant of Given Matrix: ',ele)
elif(n==2):
	print('Your matrix is of type:')
	print()
	for i in range(1,3):
		for j in range(1,3):
			print('a{}{}'.format(i,j),end=' ')
		print()
	print()
	s1=input('Enter elements of first row witha a space between:')
	l1=[int(x) for x in s1.split()]
	s2=input('Enter elements of Second row with a space between:')
	l2=[int(x) for x in s2.split()]
	det=(l1[0]*l2[1])-(l1[1]*l2[0])
	print('The determinant of given matrix:',det)
elif(n==3):
	print('Your matrix is of type')
	print()
	for i in range(1,4):
		for j in range(1,4):
			print('a{}{}'.format(i,j),end=' ')
		print()
	print()
	s1=input('Enter elements in first row elements with a space between:')
	l1=[int(x) for x in s1.split()]
	s2=input('Enter elements in second row elements with a space between:')
	l2=[int(x) for x in s2.split()]
	s3=input('Enter elements in third row elements with a space between:')
	l3=[int(x) for x in s3.split()]
	c1=l1[0]*((l2[1]*l3[2])-(l2[2]*l3[1]))
	c2=l1[1]*((l2[0]*l3[2])-(l2[2]*l3[0]))
	c3=l1[2]*((l2[0]*l3[1])-(l2[1]*l3[0]))
	det=c1-c2+c3
	print('det of given matrix is',det)
