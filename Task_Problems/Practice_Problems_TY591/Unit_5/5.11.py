inp=input('Enter two strngs with a spcae gap between them:')
list_1=inp.split()
maxlen=list_1[0]
for string in list_1:
	if(len(string)>len(maxlen)):
		maxlen=string
print('The length of the largest string is',len(maxlen))
