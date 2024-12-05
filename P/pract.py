s='jknwdo2 efjnof 3r3jnj3 3rkni j cdfjkjkef fj ej jknor jkby'
l=s.split()
l1=[]
for i in l:
    if(i[0] not in l1):
        l1.append(i[0])
l4=[]
for i in l1:
    l3=[]
    for j in l:
        if(i==j[0]):
            l3+=[j]
    l4.append(l3)
dic=dict(zip(l1,l4))
print(dic)
'''test_string=raw_input("Enter string:")
l=test_string.split()
d={}
for word in l:
    if(word[0] not in d.keys()):
        d[word[0]]=[]
        d[word[0]].append(word)
    else:
        if(word not in d[word[0]]):
          d[word[0]].append(word)
for k,v in d.items():
        print(k,":",v)'''

s='Rgukt'
for i in range(len(s)):
    for j in range(i+1):
        print(s[j],end=' ')
    print()
for i in range(len(s)-1,0,-1):
    for j in range(i):
        print(s[j],end=' ')
    print()
'''l=[]
for i in range(4):
    num=int(input('Enter an element:'))
    l.append(num)
print('maximum among four numbers is',max(l))


for i in range(1,6):
    for j in range(1,6):
        if(j<i):
            print(i,end=' ')
        else:
            print(j,end=' ')
    print()

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
'''
li=[2,3,4,5,6,7,8,9]
temp=li.copy()
for i in temp:
    fact=0
    for j in range(1,i+1):
        if(i%j==0):
            fact+=1
    if(fact==2):
        li.remove(i)
print(li)
'''

'''t=()
n=int(input('Enter a number:'))
for i in range(n):
    ele=int(input('Enter an element:'))
    t=t+(ele,)
count=0
for i in t:
    if(i%2==1):
        count+=1
li=list(t)
mini=li[0]
for i in li:
    if(i<mini):
        mini=i
t=tuple(li)
print('Count:',count)
print('Mini:',mini)
'''
'''t=()
n=int(input('Enter a number:'))
for i in range(n):
    ele=int(input('Enter an element:'))
    t=t+(ele,)
t1=()
for i in t:
    for j in range(1,i+1):
        if(i%j==0):
            fact=0
            t2=()
            for k in range(1,j+1):
                if(j%k==0):
                    fact=fact+1
            if(fact==2):
                t2=t2+(j,)
            t1=t1+t2
print(t1)

'''

'''
stry='PYTHON'
for i in range(len(stry)+1):
    for j in range(i):
        print(stry[j],end=' ')
    print()
n=int(input())
for i in range(n+1):
    print(' '*(n-i),'* '*i)
for i in range(n):
    print(' '*(i+1),'* '*(n-1-i))
'''
'''a=[1,3,2,3,1,3,1]
count=0
while(True):
    if(a!=[]):
        count+=1
    else:
        break
    a.pop(0)
print(count) 

'''
'''
for i in range(6):
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(6,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()

n=int(input('ENter a number:'))
for i in range(n+1):
    print(' '*(n-i),'* '*i)
for i in range(n):
    print(' '*(i+1),'* '*(n-1-i))
'''
'''stry=input('Enter name in caps:')
for i in range(1,len(stry)+1):
    for j in range(i):
        print(stry[j],end=' ')
    print()
'''
'''n=int(input('ENter how many terms do you want:'))
a=0
b=1
if(n<=0):
    print('Enter a valid input!')
elif(n==1):
    print(a)
else:
    l=[]
    l.append(a)
    l.append(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        l.append(c)
    print(*l,sep=',')
'''
'''a=[2,4,2,2,4,2,4,2,4]
for i in a[::-1]:
    print(i)'''
'''k=1
for i in range(1,7):
    for j in range(i):
        print(k,end=' ')
        k+=1
    print()
'''
'''a=(1,1,1,4,5,2,3,2,4,2,3,1,2,3,1,3,2,2,4,4)
a1=()
for i in a:
    if(i not in a1):
        a1=a1+(i,)
a2=()
for i in a1:
    occur=a.count(i)
    print('The number occurences of {}:{}'.format(i,occur))
    a2=a2+(occur,)
print(a2)
maxi=max(a2)
print('The element which occured in high number:{}'.format(a1[a2.index(maxi)]))
'''
'''m=int(input('ENter number of rows:'))
for i in range(m+1):
    print(' '*(m-i),'* '*i)
for i in range(m):
    print(' '*(i+1),'* '*(m-1-i))
'''
'''a=[22,44,35,'HELLO','WORLD',22,1,2,1,2,35]
print(a)
typ=int(input('ENTER WHICH TYPE OF ELEMENT OCCURENCES DO YOU WANT TO REMOVE:\n  1----To remove string type\n    2----To remove int type'))
if(typ==1):
    rem=input('ENTER ELEMENT: ')
elif(typ==2):
    rem=int(input('ENTER ELEMENT: '))
for i in a:
    if(i==rem):
        a.remove(i)
print(a)
'''
'''stry='PYTHON'
for i in range(len(stry)+1):
    for j in range(i):
        print(stry[j],end=' ')
    print()
'''
'''k=1
for i in range(6):
    for j in range(i):
        print(k,end=' ')
        k+=1
    print()
'''
'''for i in range(6):
    print('* '*i)
for j in range(5):
    print('* '*(4-j))
'''
'''for i in range(6):
    print(' '*(5-i),'* '*i)
for i in range(5):
    print(' '*(i+1),'* '*(4-i))

for i in range(1,8):
    print(' '*(7-i),'* '*i)
for j in range(6,0,-1):
    print(' '*(7-j),'* '*j)
'''

'''#(AR<STRONG)
n=int(input('ENter:'))
x=n
y=x
lenth=0
sum=0
while(n>0):
    lenth+=1
    n//=10
while(x>0):
    dig=x%10
    sum=sum+(dig**(lenth))
    x//=10
if(sum==y):
    print('ARMSTRONG')
else:
    print('NOT AN ARMSTRONG')
#(STRONG)
for j in range(1,10001):
    sum=0
    for i in range(1,j):
        if(j%i==0):
            sum+=i
    if(sum==j):
        print(j,end=' ')

n=int(input('Enter a number:'))
x=n
sum=0
while(n>0):
    dig=n%10
    fact=1
    for i in range(dig,0,-1):
        fact=fact*i
    sum+=fact
    n=n//10
if(sum==x):
    print('STRONG')
else:
    print('WEaK') 





for i in range(7):
    print(' '*(6-i),'*  '*i,end=' ')
    print()
for i in range(6):
    print(' '*(i+1),'*  '*(5-i),end=' ')
    print()



for i in range(ord('a'),ord('z')+1):
    print(chr(i))
for i in range(1,6):
    print('* '*i,end=' ')
    print()
#for i in range(1,6):
  #  for j in range(i):
 #       print('*',end=' ')
#    print()
#(SUM OF ELEMENTS IN A LIST)
i=[2,3]
Sum=0
for k in i:
    Sum+=k
print(Sum)

#(NATURA NUMBERS UPTO N)
n=int(input('ENter how many natura numbers d onyou want:'))
a=[x for x in range(1,n+1)]
print(a)

for i in range(6):
    print(' '*(5-i),'* '*i,end=' ')
    print()
for j in range(5):
    print(' '*(j+1),'* '*(4-j),end=' ')
    print()

for i in range(6):
    print('* '*i,end=' ')
    print()
for j in range(5):
    print('* '*(4-j),end=' ')
    print()


stry='PYTHON'
for i in range(len(stry)):
    for j in range(i+1):
        print(stry[j],end=' ')
    print()

k=1
for i in range(1,6):
    for j in range(i):
        print(k,end=' ')
        k+=1
    print()

for i in range(1,6):
    for j in range(i):
        print('*',end=' ')
    print()

for i in range(1,6):
    print('* '*i,end=' ')
    print()

i=1
while(i<=5):
    j=1
    while(j<=i):
        print('*',end=' ')
        j+=1
    print()
    i+=1


a=input('Enter a long number without commas and spaces:')
a=list(a)
print('list=',a)

(MINI<MAXI<SUM<LENGTH<AVG<PROGRAM)
n=[1,25,1,3,1,5,8,3,5]
sum=0
lenth=0
mini=n[0]
maxi=n[-1]
for i in n:
    lenth+=1
    sum+=i
    if(i<mini):
        mini=i
    if(maxi<i):
        maxi=i
print('lenth=',lenth,'sum=',sum,'minimum=',mini,'maximum=',maxi)
avg=sum/lenth
print('The average is %.3f'%avg)

for i in range(1,101):
    if(i%2==0):
        if(i==100 or i==100-1):
            print(i)
        else:
            print(i,end=",")

f=int(input("Enter first numebr:"))
s=int(input("Enter second numebr:"))
n=int(input("Enter upto how many terms do you want:"))
print(f,s,sep='\n')
for i in range(2,n):
    t=f+s
    print(t)
    f=s
    s=t


n=int(input("Enter a number:"))
last=n%10
print("Last number is",last)
while(n>9):
    n=n//10
print('First digit is',n)
#(RECURSION EXPONENT)
def exponent(x,y):
    expo=x
    pow=0
    if(pow==y):
        print(expo)
    else:
        pow+=1
        expo*exponent(x,y)
exponent(2,3)
#(RECURSION FIBONACCI)
def fibonacci(a,b,n):
    print(a,b,sep=',',end=',')
    c=a+b
    a=b
    b=c
    if(c>n):
        print(c)
    else:
        fibonacci(a,b,n)
fibonacci(1,1,25)


i=int(input("Enter a number:"))
k=i
m=k
lent=0
while(i>0):
	dig=i%10
	lent+=1
	i//=10
Sum=0
while(k>0):
	digi=k%10
	Sum=Sum+(digi**lent)
	k//10
if(Sum==m):
	print("Armstrong")


#(STAAAAAAAAAAAR PATTERNNNNNNNN)

for j in range(7):
    print(" "*(6-j),"* "*j,end=" ")
    print()
for j in range(6):
    print(" "*(j+1),"* "*(5-j),end=" ")
    print()

#(RGUKT PATTERN)
k='RGUKT'
for i in range(1,len(k)+1):
    for j in range(i):
        print(k[j],end=" ")
    print()



#(Sorting a ist without using sort method)
l=[9,3,46,342,23,24,132,5,1,13,3]
l1=[]
for i in range(len(l)):
    ind=l.index(min(l))
    k=l.pop(ind)
    l1.insert(0,k)
print(l1)


#(STRING PATTERN)
n=input("Enter:")
for i in range(len(n)):
    for j in range(i+1):
        print(n[j],end=" ")
    print()    

#(NUMBER PATTERN)
k=1
n=int(input("Enter a number:"))
for i in range(n):
    for j in range(i):
        print(k,end=" ")
        k+=1
    print()

#(PATTERN PROGRAM)
for j in range(7):
    print(" "*(6-j),"* "*j,end=" ")
    print()
for j in range(7):
    print(" "*j,"* "*(6-j),end=" ")
    print()

#(parallelogram pattern)
#for j in range(7):
#    print(" "*(6-j),"*"*j,end=" ")
#    print()
#for j in range(7,0,-1):
#    print("*"*j," "*(6-j),end=" ")
#    print()


#(FIBONACCI SERIES)
a=int(input("ENter a number:"))
b=int(input("Enter another number:"))
print(a,b,sep=",",end=",")
i=0
while(i<7):
    c=a+b
    print(c,end=",")
    a=b
    b=c
    i+=1
#(STRONG NUMBER)
n=int(input("ENter a numebr:"))
y=n
sum=0
while(n>0):
    dig=n%10
    fact=1
    for i in range(dig,0,-1):
        fact=fact*i
    sum+=fact
    n//=10
if(sum==y):
    print("STRNG")

r="bw"
l="sw"
r,l=l,r
print(r)

#(NUMBER PALINDROME)
n=int(input("Enter a numebr:"))
print(n)
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n//=10
print(rev)


n=input("Eter your name:")
num=int(input("Enter how many times do you want to repeat your name:"))
i=0
while(i<num):
    print(n)
    i+=1

num=int(input("Enter upto many nums do you want t0 print natural numbers:"))
print("natural numbers upto %d"%num)
i=1
while(i<num+1):
    print(i)
    i+=1 

#(PATTERNS)
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()

i=1
while(i<6):
    j=1
    while(j<i+1):
        print("*",end=" ")
        j+=1
    i+=1
    print()
#(SUM OF ODD NUMEBRS)
Sum=0
for i in range(1,10):
    if(i%2==1):
        print(i)
        Sum+=i
print(Sum)
#n1=int(input("Enter how many numbers to you want enter:"))
#li1=[]
#for i in range(n1):
#    x=int(input("Enter a number:"))
#    li1.append(x)
#print("Original list is",li1)
#for i in range(1,n1):
#    fact=0
#    for j in range(1,i+1):
#        if(i%j==0):
#            fact+=1
#    if(fact==2 and i<n1):
#        k=li1[i]
#        li1.remove(k)
#print("List after removing prime indices is",li1)


print("--------------COMMON ELEMENTS IN TWO LISTS----------------")
n1=int(input("Enter how many numbers to you want enter:"))
li1=[]
for i in range(n1):
    x=int(input("Enter a number:"))
    li1.append(x)
li1.sort()
n2=int(input("Enter how many numbers to you want enter:"))
li2=[]
for i in range(n2):
    x=int(input("Enter a number:"))
    li2.append(x)
li2.sort()
for i in li1:
    for j in li2:
        if(i==j):
            print("TRUE")
            break
    break
else:
    print("NO COMMON ELEMENt")

print("--------------MAX MIN UDF-----------")
n=int(input("Enter hpw many numbers to you want enter:"))
li=[]
for i in range(n):
    x=int(input("Enter a number:"))
    li.append(x)
li.sort()
print("The max num is",li[-1])
print("The max num is",li[0])

print("----------------SUM AND MULTIPLICATION OF ALL ELEMENTS(DEF)----------------")
n=int(input("Enter hpw many numbers to you want enter:"))
li=[]
for i in range(n):
    x=int(input("Enter a number:"))
    li.append(x)
li.sort()
sum=0
for i in li:
    sum+=i
print("sum is",sum)

print("----------------MEDIAN(DEF)----------------")
n=int(input("Enter hpw many numbers to you want enter:"))
li=[]
for i in range(n):
    x=int(input("Enter a number:"))
    li.append(x)
li.sort()
m1=int(n/2)
m2=int((n/2)-1)
if(n%2==0):
    print("THe median(s) of entered numbers are",li[m1],"and",li[m2])
else:
    print("The medians(s) of entered numbers are",li[m1])

print("----------------SUM OF NATURAL NUMBERS(DEF)----------------")
def sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
n=int(input("Enter a number:"))
print("The sum of natural numbes up to {} is {}".format(n,sum(n)))

print("-----------------GREATEST COMMON DEVISER-----------------")
def gcd(a,b):
    rem=a%b
    if(rem==0):
        return b
    else:
        return gcd(b,rem)
print("the greatest common deviser of entered numbers is",gcd(6,4))
def hello(a):
    if(a==1):
        return a
    if a!=1:
        return a+hello(a-1)
x=int(input("Enter a number to print n numbers(n):"))
print(hello(x))
print("-------------------RECURSIVE FORMULA----------------")
def fact(a):
    if a==1 or a==0:
        return 1
    else:
        return a*fact(a-1)
n=int(input("Enter a number to find its factorial:"))
print(fact(n))

print("---------------PRinting a LIST-----------------")
n=int(input("Enter range of numbers;"))
li=[]
for i in range(n):
    k=int(input("Enter a number:"))
    li.append(k)
print(li)
print("-------------------------REVERSING A LIST-------------------------")
n=int(input("Enter range of number:"))
li=[]
for i in range(n):
    k=int(input("Enter a number:"))
    li.append(k)
print(li)
li.sort()
print(li)
print(li[::-1])
li.sort(reverse=True)
print(li)
print("--------------ADDING AND REMOVING ELEMENTS--------------------")
a=[1,2,3,48,2,6,4]
a.append(2022)
print(a)
a.remove(48)
print(a)

print("-------------------SUM OF EACH ELEMENT-------------------")
n=int(input("Enter range of numbers;"))
li=[]
for i in range(n):
    k=int(input("Enter a number:"))
    li.append(k)
nli=[]
for i in li:
    sum=0
    while(i>0):
        dig=i%10
        sum+=dig
        i//=10
    nli.append(sum)
print(nli)


print("-------------------FACTORIAL OF EACH ELEMENT-------------------")
n=int(input("Enter range of numbers;"))
li=[]
for i in range(n):
    k=int(input("Enter a number:"))
    li.append(k)
nli=[]
for i in li:
    fact=1
    for j in range(i,0,-1):
        fact=fact*j
    nli.append(fact)
print(nli)

print("-------------------FIRST AND LAST DIGIT OF EACH ELEMENT-------------------")
n=int(input("Enter range of numbers;"))
li=[]
for i in range(n):
    k=int(input("Enter a number:"))
    li.append(k)
if(li[0]==6 or li[-1]==6):
    print("YES")
else:
    print("NO")


a="tharu  hf"
a1=a.center(100)
print(a1)
print(max(a))
print(a.split("$",1))
print(min(a))
print(a.count("t",2,4))
print("PAlidrome without looooop")
a=input("Enter a number")
b=a[::-1]
if(a==b):
    print("PAlindrome")
s=''
for i in range(1,len(a)+1):
    s+=a[len(a)-i]
if(s==a):
    print("PALIDROMMMMMMMMMMMMMMMMMMMMMME")
print("----------------------PERFECT NUMBER----------------------")
n=int(input("Enter a number:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
if(sum==n):
    print("It is a Perfect Number")
else:
    print("It is not a Perfect Number")
print("----------------FIBONACCI SEQUENCE--------------")
a=int(input("ENter a number"))
b=int(input("Enter a numbers"))
print(a,b,end=",")
for i in range(6):
    c=a+b
    print(c,end=",")
    a=b
    b=c
print(end="\b")
print()
print("-------------STRONG NUMBER---------------")
n=int(input("ENter a number:"))
sum=0
x=n
while(n>0):
    dig=n%10
    fact=1
    for i in range(dig,0,-1):
        fact=fact*i
    sum=sum+fact
    n//=10
if(sum==x):
    print("Its very strong")
else:
    print("Its not that much strong,baby Try Again")





print("------------DAIMOND SHAPE-----------")
for i in range(7):
    print(" "*(6-i)," *"*i,end="")
    print()
for i in range(7):
    print(" "*(i+1)," *"*(5-i),end="")
    print()






print("---------String PATTERN------------")
n=input("ENter your name in caps:")
for i in range(len(n)):
    for j in range(i+1):
        print(n[j],end=" ")
    print()
#def fact(n):
#    for i in range(1,n+1):
#        if(n%i==0):
#            print(i)
#a=int(input("Enter a number:"))
#while(a>0):
#    d=a%10
#    fact(d)
#    a//=10
print("-----------FACTORS FOR EACH DIGIT IN  GIVEN NUMBER----------")
n=int(input("Enter a Number:"))
x=n
li=[]
while(n>0):
    digit=n%10
    for i in range(1,digit+1):
        if(digit%i==0):
            li.append(i)
    print("Factorail for {} in number {} :{}".format(digit,x,li))
    n//=10
    li.clear()
print("--------FACTORIALS OF EACH DIGIT IN NUMBER--------")
n=int(input("Enter a number:"))
digit=0
while(n>0):
    digit=digit%10
    fact=1
    for i in range(digit,0,-1):
        fact=fact*i
    print(fact)
    n=n//10
print("-----------FACTORIALS AND FACTORS FOR ALL EVEN NUMBERS IN GIVEN RANGE-------------")
start=int(input("Enter a start value:"))
end=int(input("Enter end value:"))
for i in range(start,end+1):
    if(i%2==0):
        fact=1
        for k in range(i,0,-1):
            fact=fact*k
        print("Factorial for {} is {}".format(i,fact))
        li=[]
        for j in range(1,i+1):
            if(i%j==0):
                li.append(j)
        print("factors for  {} is/are {}".format(i,li))
        print()
print("--------------factors and factorials for given number------------")
n=int(input("Enter a number:"))
fact=1
for i in range(n,0,-1):
    fact=fact*i
print("Factorial for given number is",fact)
li=[]
for i in range(1,n+1):
    if(n%i==0):
        li.append(i)
print("factors for given number is/are",li)

print("--------------Factors for every number in given interval--------------")
start=int(input("ENter start value:"))
end=int(input("ENter end value:"))
li=[]
for k in range(start,end+1):
    for i in range(1,k+1):
        if(k%i==0):
            li.append(i)
    print("Factors for {} are {}".format(k,li))
    li.clear()        
print("----------PRIME FACTORS--------------")
n=int(input("Enter a number:"))
for i in range(1,n+1):
    if(n%i==0):
        fact=0
        for k in range(1,i+1):
            if(i%k==0):
                fact+=1
        if(fact==2):
            print(i)
print("--------------FACTORIAL-------------")
n=int(input("Enter any number:"))
fact=1
for i in range(n,0,-1):
    fact=fact*i
print("Factorial of {} is {}".format(n,fact))
print("------------AVERAGE,MIN and MAX FROM LIST----------------")
n=int(input("Enter length of list:"))
l=[]
sum=0
for i in range(n):
    k=int(input("Enter a value"))
    l.append(k)
    sum=sum+k
print('sum is',sum)
print(min(l))
print(max(l))
print("-----------NUMBER PATTERN--------------")
n=int(input("Enter A Number:"))
k=1
for i in range(0,n):
    for j in range(0,i+1):
        print(k,end=" ")
        k+=1#if we place this updation in first loop,we will get same numbers in each line
    print() 
print()
print("-----------FIBONACCI SERIES--------------")
n=int(input("Enter A Number"))
a=0
b=1
print(a,b,end=" ")
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
print("---------PRinting characters form a to z------------")
i=97
while(i<=122):
    print(chr(i),end=" ")
    i+=1
print()
print("---------------No.of factors for given number-----------")
n=int(input("enter a number"))
fact=0
for i in range(1,n+1):
    if(n%i==0):
        fact+=1
        print(i)
print("Number of factors are {}".format(fact))
print("---------Whether it is prime or not---------")
n=int(input("Enter a number:"))
c=0
fact=0
for i in range(1,n+1):
    if(n%i==0):
        fact+=1
if(fact==2):
    print("It is a PRime Number")
else:
    print("It is not a prime number")
print("------Nested Lopp Example---------")
for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print()
i=0
while(i<=6):
    j=0
    while(j<=i):
        print("*",end=" ")
        j+=1
    print()
    i+=1
print("------------printing n numbers with for loop-------------")
n=int(input("Enter A Number:"))
for i in range(1,n):
    print(i,end=" ")

print("------------printing sum of numbers in a list-------------")
num=[1,2,3,4,4,5]
sum=0
for i in num:
    sum+=i
print(sum)

print("------------printing even numbers up to n-------------")
n=int(input("Enter A Number:"))
i=1
while(i<n+1):
    print(i,end=" ")
    i+=1
print("------------printing n natural numbers-------------")
n=int(input("Enter A Number:"))
i=1
while(i<n+1):
    print(i,end=" ")
    i+=1
print("------------name printing upto n times-------------")
n=int(input("Enter A NUmber: "))
i=0
while(i<n+1):
    print("RGUKT")
    i+=1
else:
    print("Good Bye")'''
