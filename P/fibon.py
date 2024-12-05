def fibon(n):
	n1,n2=0,1
	l=[]
	if(n<=0):
		print('sorrrrrrrrrrry')
	else:
		for i in range(1,n+1):
			if(n1<n):
				l.append(n1)
			n3=n1+n2
			n1=n2
			n2=n3
	return(l)
n=int(input('Enter upto which number do you want fibonacci series:'))
print(*fibon(n),sep=',')


