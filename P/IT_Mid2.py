'''
#(--------------------IT First Question---Sub Question A-------------------------------)
n=int(input('ENter a Number to find its factorial:'))
i=n
fact=1
while(i!=0):
	fact=fact*i
	i-=1
print('The factorial of {} is {}'.format(n,fact))
#(--------------------IT First Question---Sub Question B-------------------------------)
n=int(input('ENter a Number to find its factors:'))
print('The factors of Given number are')
for i in range(1,n+1):
	if(n%i==0):
		print('\t\t\t\t',i)
#(--------------------IT Third Question---Sub Question A-------------------------------)
l=[]
for i in range(4):
    num=int(input('Enter an element:'))
    l.append(num)
print('maximum among four numbers is',max(l))

(or)
n1=int(input('Enter first number:'))
n2=int(input('Enter second number:'))
n3=int(input('Enter third number:'))
n4=int(input('Enter second number:'))
if(n1>=n2 and n1>=n3 and n1>=n4):
	print(n1,'is the Greatest Among the Four')
elif(n2>=n3 and n2>=n4):
	print(n2,'is the Greatest among the Four')
elif(n3>=n4):
	print(n3,'is the Greatest among the Four')
else:
	print(n4,'is the Greatest among the Four')
	
#(--------------------IT Third Question---Sub Question B-------------------------------)
num=int(input('Enter:'))
while(num%2==0):
	while(num%4==0):
		while(num%8==0):
			print('DIVISIBLE')
			break
		else:
			print('NOT DIVISIBLE BY 8')
		break
	else:
		print('NOT DIVISIBLE BY 4 and 8')
	break
else:
	print('NOT DIVISIBLE BY 2,4 and 8')

#(--------------------IT Fifth Question---Sub Question A--------------------------------)
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

#(--------------------IT Fifth Question---Sub Question B--------------------------------)
n=int(input('Enter a number:'))
l=[x for x in range(2,n+1,2)]
print(l)
#(--------------------IT Seventh Question---Sub Question A------------------------------)
t=()
n=int(input('Enter a number:'))
for i in range(n):
    ele=int(input('Enter an element:'))
    t=t+(ele,)
t1=();t2=();c=()
for i in t:
    for j in range(1,i+1):
        if(i%j==0):
            fact=0
            for k in range(1,j+1):
                if(j%k==0):
                    fact=fact+1
            if(fact==2):
                t2=t2+(j,)
    t1=t1+(t2,)
    c=c+((i,)+(t2,))
    t2=()
print(c)
print(t1)
'''
#(---------------------IT Seventh Question---Sub Question B-----------------------------)
t=()
n=int(input('Enter a number:'))
for i in range(n):
	ele=int(input('Enter an element:'))
	t=t+(ele,)
count=0
for i in t:
	if(i%2==1):
		count+=1
mini=t[0]
for i in t:
	if(i<mini):
		mini=i
print('Count od Odd Elements: ',count)
print('Minimum Element of the List:',mini)
'''
#(----------------------IT Eighth Question---Sub Question A-----------------------------)
t=['a','b','c','d','e','f']
print('I.',t[-3::-1])
print('II.',t[2::-1])
print('III.',t[2::1])
print('IV.',t[:4:-2])
print('V.',t[:-4:-2])
#(----------------------IT Eighth Question---Sub Question B-----------------------------)
for i in range(1,6):
	for j in range(1,6):
		if(j<i):
			print(i,end=' ')
		else:
			print(j,end=' ')
	print()
'''
