n1=input('Enter Your name :')
n2=input('Enter another Name : ')
s1='';s2=''
for i in n1:
	if(i!=' '):
		s1+=i
for i in n2:
	if(i!=' '):
		s2+=i
s3=s1.lower()+s2.lower()
s4=list(s3)
for i in s4:
	if(s4.count(i)%2==0):
		for k in range(s4.count(i)):
			s4.remove(i)
	else:
		for k in range(1,s4.count(i)):
			s4.remove(i)
f=['f','l','a','m','e','s']
l1=len(s4)
l2=len(f)
while(True):
	if(l1>l2):
		c=l1%l2
	else:
		c=l1
	f.pop(c-1)
	temp=f.copy()
	for i in temp:
		if(temp.index(i)<(c-1)):
			f.remove(i)
			f.append(i)
	l2=len(f)
	if(len(f)==1):
		break
if('f' in f):
	print('{} and {} are Frineds'.format(n1,n2))
elif('l' in f):
	print('{} and {} are Lovers'.format(n1,n2))
elif('a' in f):
	print('Attraction')
elif('m' in f):
	print('Marriage')
elif('e' in f):
	print('{} and {} are Enemies'.format(n1,n2))
elif('s' in f):
	print('{} and {} are Sisters'.format(n1,n2))
else:
	print('Sorry')
