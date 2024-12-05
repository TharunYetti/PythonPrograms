n=int(input('Enter order of Matrix :'))
print()
for i in range(1,n+1):
	for j in range(1,n+1):
		print('a{}{}'.format(i,j),end=' ')
	print()
print()
L1=[]
L2=[]
print('Enter first Matrix>>>>')
for i in range(1,n+1):
	ele=input('Enter elements of {} row with a space between :'.format(i))
	l1=[int(x) for x in ele.split()]
	if(len(l1)==n):
		L1.append(l1)
	else:
		print('This Row doesn\'t cotain {} elements to add!!!So you have to interupt and try again Otherwise It wil raise an an error'.format(n))
print('Now enter another matrix elements to add>>>>')
for j in range(1,n+1):
	ele2=input('Enter elements of {} row with a space between :'.format(j))
	l2=[int(x) for x in ele2.split()]
	if(len(l2)==n):
		L2.append(l2)
	else:
		print('This Row doesn\'t cotain {} elements to add!!!So you have to interupt and try again Otherwise It wil raise an an error'.format(n))
for i in range(n):
	for j in range(n):
		print(L1[i][j]+L2[i][j],end=' ')
	print()
