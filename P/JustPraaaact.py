j='HELLO'
l=list(j)
length=0
i=0
while(True):
    if(l==[]):
        break
    else:
        length+=1
    del l[0]    
print(length)





















'''#(ALPHA PATTERN)
n=input('ENter your name in caps:')
for i in range(len(n)):
    for j in range(i+1):
        print(n[j],end=' ')
    print()
#(NUMBER PATTERN)
n=int(input('Enter a number:'))
k=1
for i in range(1,n):
    for j in range(i):
        print(k,end=' ')
        k+=1
    print()
#(DAIMOND PATTERN)
for i in range(6):
    print(' '*(5-i),'* '*i,end=' ')
    print()
for i in range(5):
    print(' '*(i+1),'* '*(4-i),end=' ')
    print()
#(HALF DAIMOND PATTERN)
for i in range(5):
    print('* '*i,end=' ')
    print()
for j in range(5,0,-1):
    print('* '*j,end=' ')
    print()
#(TRAINGLE PATTERN)
n=int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(i):
        print('!',end=' ')
    print()
#(ATTENDANCE PERECNTAGE)
noh=int(input('No.of classes held:'))
noa=int(input('No.of classes attended:'))
perc=noa/noh
print(perc)
if(perc>75):
    print('OK')
else:
    print('Not OK')

#(EVEORODD)
n=int(input("ENter a number:"))
if(n%2==0):
    print('Even')
else:
    print('Odd')

#(DIVISIBLE BY 7 AND 5)
n=int(input("ENter a number:"))
if(n%7==0 and n%5==0):
    print('Yes')
else:
    print('NO')'''