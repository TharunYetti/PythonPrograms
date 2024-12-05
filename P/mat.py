n=int(input('enter order of matrix:'))
if(n==1):
	s1=int(input('Enter element of first matrix:'))
	s2=int(input('Enter element of second matrix:'))
	print('Sum of two matrix is [{}]'.format(s1+s2))
elif(n==2):
	print('Your supposed matrix is')
	for i in range(1,3):
		for j in range(1,3):
			print('a{}{}'.format(i,j),end=' ')
		print()
	print()
	s1=input('Enter First row elements seperating with a space :')
	l1=s1.split()
	s2=input('Enter second row elements seperating with a space :')
	l2=s2.split()
	print('Now enter other matrix to addition:')
	s3=input('Enter Third row elements seperating with a space:')
	l3=s3.split()
	s4=input('Enter Third row elements seperating with a space:')
	l4=s4.split()
	for i in range(2):
		print(int(l1[i])+int(l3[i]),end=' ')
	print()
	for i in range(2):
		print(int(l2[i])+int(l4[i]),end=' ')
	print()
elif(n==3):
	for i in range(1,4):
		for j in range(1,3+1):
			print('a{}{}'.format(i,j),end=' ')
		print()
	print()
	l1,l2,l3,l4,l5,l6=[],[],[],[],[],[]
	s1=input('Enter First row elements seperating with a space :')
	l1=s1.split()
	s2=input('Enter second row elements seperating with a space:')
	l2=s2.split()
	s3=input('Enter Third row elements seperating with a space:')
	l3=s3.split()
	print('Now enter other matrix to addition:')
	s4=input('Enter First row elements seperating with a space:')
	l4=s4.split()
	s5=input('Enter Second row elements seperating with a space:')
	l5=s5.split()
	s6=input('Enter Third row elements seperating with a space:')
	l6=s6.split()
	for j in range(3):
		print(int(l1[j])+int(l4[j]),end=' ')
	print()
	for j in range(3):
		print(int(l2[j])+int(l5[j]),end=' ')
	print()
	for j in range(3):
		print(int(l3[j])+int(l6[j]),end=' ')
	print()
else:
	print('Please select among 1,2 and 3')
