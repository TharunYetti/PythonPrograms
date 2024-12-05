options={'A':['  *  ',' * * ','*****','*   *','*   *'],'B':['**** ','*   *','*****','*   *','**** '],'C':[' ** ','*  *','*   ','*  *',' ** ']}
'''
def _65():
    print('  ','*','  ')
    print('','*',' ','*','')
    print('*','   ','*')
    print('*','   ','*')
    print('*','*','*','*')
    print('*','   ','*')
    print('*','   ','*')
def _66():
    print('*','*','*','')
    print('*','  ','*')
    print('*','  ','*')
    print('*','*','*','')
    print('*','  ','*')
    print('*','  ','*')
    print('*','*','*','')
def _67():
    print('','*','*','*')
    print('*',' ',' ','*')
    print('*')
    print('*')
    print('*')
    print('*',' ',' ','*')
    print('','*','*','*')
_67()
'''
'''
def alph(n):
    alpha={65:_65()}
    alpha[n]
a=input('Enter:')
for i in range(65,98):
    for j in a:
        if(i==ord(j)):
            alph(i)
'''










'''
n=int(input('Enter a number:'))
for i in range(1,n+1):
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()

n=int(input('Enter a number'))
for i in range(n+1):
    print(' '*(n-i),'* '*(i))
for i in range(n):
    print(' '*(i+1),'* '*(n-1-i))

k=1
for i in range(1,6):
    for j in range(i):
        print(k,end=' ')
        k+=1
    print()

l='PYTHON'
for i in range(1,len(l)+1):
    for j in range(i):
        print(l[j],end=' ')
    print()


def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
print(fact(4))

d=[3,[5,5]]
print(d[1][0])

i=1
while(i<=5):
    j=1
    while(j<=i):
        print('OK',end=' ')
        j+=1
    i+=1
    print()

k='RgUkT'
for i in range(1,len(k)+1):
    for j in range(i):
        print(k[j],end=' ')
    print()
for i in range(len(k)-1,0,-1):
    for j in range(i):
        print(k[j],end=' ')
    print()
'''



'''
inp=input('Enter elements with a space gap between:')
l=inp.split()
l2=[]
new={}
for i in l:
    if(i[0] not in l2):
        l2.append(i[0])
for i in l2:
    tup=()
    for j in l:
        if(i==j[0]):
            tup+=(j,)
    new[i]=tup
print(new)



a=0
b=1
n=int(input('Enter a number'))
if(n<=0):
    print('Enter a positive number')
elif(n==1):
    print(a,end=' ')
else:
    print(a,b,sep=' ',end=' ')
    for i in range(2,n):
        c=a+b
        print(c,end=' ')
        a=b;b=c
    print()



for i in range(1,6):
    for j in range(i):
        print('*',end=' ')
    print()

i=1
while(i<=5):
    j=0
    while(j<i):
        print('*',end=' ')
        j+=1
    i+=1
    print()


n1=int(input('Enter first number:'))
n2=int(input('Enter second number:'))
n3=int(input('Enter third number:'))
n4=int(input('Enter fourth number:'))
if(n1>=n2 and n1>=n3 and n1>=n4):
    print(n1,'is the greatest number')
elif(n2>=n3 and n2>=n4):
    print(n2,'is the greatest number')
elif(n3>=n4):
    print(n3,'is the greatest number')
else:
    print(n4,'is the greatest number')


li=[]
for i in range(1,5):
    inp=int(input('Enter #{} number:'.format(i)))
    li.append(inp)
print(max(li),'is the largest number')
'''