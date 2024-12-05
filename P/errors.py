options={'A':['  *  ',' * * ','*   *','*   *','*****','*   *','*   *'],'B':['**** ','*   *','*   *','*****','*   *','*   *','**** '],'C':[' *** ','*   *','*    ','*    ','*    ','*   *',' *** '],'D':['**** ','*   *','*   *','*   *','*   *','*   *','**** '],'E':['*****','*   *','*    ','**** ','*    ','*   *','*****'],'F':['*****','*    ','*    ','**** ','*    ','*    ','*    '],'G':[' *** ','*  * ','*    ','*    ','* ***','*   *',' ** *'],'H':['*   *','*   *','*   *','*****','*   *','*   *','*   *'],'I':['*****','  *  ','  *  ','  *  ','  *  ','  *  ','*****'],'J':[' ****','    *','    *','    *','*   *','*   *','*****'],'K':['*    *','*   * ','*  *  ','* *   ','** *  ','*   * ','*    *'],'L':['*    ','*    ','*    ','*    ','*    ','*    ','*****'],'M':['**   **','*  *  *','*  *  *','*  *  *','*     *','*     *','*     *'],'N':['*      *','* *    *','*  *   *','*   *  *','*    * *','*      *','*      *'],'O':['*****','*   *','*   *','*   *','*   *','*   *','*****'],'P':['*** ','*  *','*  *','*** ','*   ','*   ','*   '],'Q':[' **  ','*  * ','*  * ','*  * ','* ** ',' *** ','    *'],'R':['**** ','*   *','*   *','*  * ','***  ','*  * ','*   *'],'S':[' *** ','*   *','*    ',' *** ','    *','*   *',' *** '],'T':['*******','   *   ','   *   ','   *   ','   *   ','   *   ','   *   '],'U':['*   *','*   *','*   *','*   *','*   *','*   *',' *** '],'V':['*           *',' *         * ','  *       *  ','   *     *   ','    *   *    ','     * *     ','      *      '],'W':['*       *','*       *','*       *','*   *   *',' *  *  * ','  * * *  ','  ** **  '],'X':['*     *',' *   * ','  * *  ','   *   ','  * *  ',' *   * ','*     *'],'Y':['*   *','*   *','*   *',' * * ','  *  ','  *  ','  *  '],'Z':['*****','    *','   * ','  *  ',' *   ','*    ','*****'],' ':['     ','     ','     ','     ','     ','     ','     ']}
def pr(n):
    for i in range(7):
        for j in range(len(n)):
            print(options[n[j]][i]+'  ',end=' ')
        print()
name=input('Enter an alphabet:')
pr(list(name.upper()))
'''

rows=5
for i in range(rows):
    for j in range(i+1):
        print(i+1,end=' ')
    print()
rows=5
for i in range(5):
    k=1
    for j in range(i+1):
        print(k,end=' ')
        k+=1
    print()
rows=5
k=1
for i in range(5,0,-1):
    for j in range(i):
        print(k,end=' ')
    print()
    k+=1
for i in range(rows,0,-1):
    for j in range(i):
        print(5,end=' ')
    print()
for i in range(1,rows+1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
for i in range(rows):
    for j in range(i+1):
        print('*',end=' ')
    print()


for i in range(rows):
    for j in range(rows,i,-1):
        print(j,end=' ')
    for m in range(i):
        print('   ',end=' ')
    for l in range(i+1,rows+1):
        print(l,end=' ')
    print()


k=1
for i in range(6):
    print(' '*(5-i),'* '*i) if(i<3) else print(' '*(5-i),'*',' '*k,'*')
    k+=1
for j in range(5):
    print(' '*(j+1),'* '*(4-j))


for i in range(6):
    print('* '*i)
for j in range(5):
    print('* '*(4-j))

for i in range(6):
    print(' '*(5-i),'*'*i)
for i in range(5):
    print(' '*(i+1),'*'*(4-i))



for i in range(1,6):
    print('*'*(6-i),'__'*(i-1),'*'*(6-i))

for i in range(rows):
    for j in range(rows,i,-1):
        print('*',end=' ')
    for m in range(i):
        print('____',end='')
    for l in range(i+1,rows+1):
        print('*',end=' ')
    print()

'''




'''

a='abcdefghij'
l=list(a)
l1=[]
i=0
while(i<len(l)):
    l1.append(l[i]+l[i+1])
    i+=2
print(l1)


'''
'''
try:
    a=int(input('Enter:'))
    if(a<0):
        raise (TypeError('Th9sj is a typo'))
except TypeError as t:
    print(t)
finally:
    print('Skjniubyvady')
'''
'''#(count of a character in the file)
f=open('Hello.txt','r')
inp=int(input('Enter a number:'))
k=f.read()
print(k)
f.close()
c=0
for i in k:
    if(str(inp)==i):
        c+=1
print(c)
print(k.count(str(inp)))
'''

'''
k='RGUKT'
for i in range(len(k)):
    for j in range(i+1):
        print(k[j],end=' ')
    print()
for i in range(len(k)-1,0,-1):
    for j in range(i):
        print(k[j],end=' ')
    print()
'''

'''
inp=input('ENter a string:')
l=inp.split();l1=[]
print(l)
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
f=[l.count(p) for p in l1]
print(f)
d={x:l.count(x) for x in l1}
print(d)
'''
'''k=1
for i in range(1,6):
    for j in range(i):
        print(k,end=' ')
        k+=1
    print()

for i in range(1,6):
    print(' '*(6-i),'* '*i)
for j in range(5):
    print(' '*(1+j),' *'*(4-j))


h='PYTHON'
for i in range(len(h)):
    for j in range(i+1):
        print(h[j],end=' ')
    print()
'''
'''
a,b=1,2
n=int(input('Enter how many terms do you want:'))
if(n<=0):
    print('Please enter a vaid number!')
else:
    for i in range(1,n+1):
            print(a,end=' ')   
            c=a+b
            a=b
            b=c
'''

'''
def fact(n):
    prod=1
    for i in range(1,n+1):
        prod*=i
    return prod
n=int(input('Enter a number:'))
for num in range(n+1):
    temp1=num
    temp2=num
    sum=0
    while(temp2>0):
        dig=temp2%10
        sum=sum+fact(dig)
        temp2//=10
    if(num==sum):
        print(num,end=' ')
'''

'''
d={'a':'Tarun','b':'yguys','c':'widef'}
value_list=list(d.values())
str1=''
for i in d.keys():
        str1+=i
key_list=list(str1.replace('a','D'))
print('Original dictionary is',d)
print('New dectionary is',dict(zip(key_list,value_list)))
'''















'''l=[3,"a"]
o=l.sort()
print(o)'''
"""print(l)
try:
    a=int('x')
except ValueError:
    print('v')
finally:
    print('Happy brithday')
    raise TypeError('45')
if('k'>'d'):
    print('OK')
else:
    print('Not Ok')"""
