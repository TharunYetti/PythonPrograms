#(IT First Question---Sub Question A)
n=int(input('ENter a Number to find its factorial:'))
i=n
fact=1
while(i!=0):
	fact=fact*i
	i-=1
print(fact)
print('The factorial of {} is {}'.format(n,fact))
'''
#()
A=[3,4,5,6,7,8]
temp=A.copy()
posi=1
for i in temp:
    l=[]
    for j in range(1,i+1):
        if(i%j==0):
            l.append(j)
    A.insert(posi,l)
    posi+=2
print(A)
'''
