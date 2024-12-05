inp=input('Enter two strngs with a spcae gap between them:')
list_1=inp.split()
list_2=[]
for string in list_1:
	length=0
	for j in string:
		length+=1
	list_2+=[length]
if(list_2[0]>list_2[1]):
	print(repr(list_1[0]),'is the largest string')
else:
	print(repr(list_1[1]),'is the largest string')
