'''import turtle as t
def square(a=0,b=0,color='black'):
    t.penup()
    t.goto(a,b)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.end_fill()
    t.backward(100)
    t.left(90)
    t.backward(100)
    t.left(90)
    t.backward(100)
    t.left(90)
    t.backward(100)
    t.left(90)
    t.goto(0,0)
square(-200,200,'red')
square(200,100,'red')
'''
'''def ser():
    n=int(input('Enter the Number1:'))
    m=int(input('Enter the Number2:'))
    o=int(input('How many terms do you want:'))
    i=1
    print('the fibonacci series up to n numbers',n,m,end=' ')
    while(i<=o):
        p=n+m
        n=m
        m=p
        i+=1
        print(p,end=' ')
ser()'''


'''s='Hello';l=[];ns=''
for i in s:
    l.insert(-1,i)
for j in l:
    ns+=j
print(ns)

print('hello\rworld')

'''
import random as r
import turtle as t
l=['blue','green','red','orange','yellow','indigo']
t.bgcolor('black')
t.pensize(2)
t.hideturtle()
t.speed(250)
for i in range(125):
    t.color(r.choices(l))
    t.circle(i)
    t.right(2)
    t.forward(2)
t.penup()
t.left(125*2)
t.goto(0,0)
t.pendown()
for i in range(125):
    t.color('white')
    t.circle(i)
    t.right(2)
    t.forward(2)
t.penup()
t.left(125*2)
t.goto(0,0)
t.pendown()
t.showturtle()
for i in range(125):
    t.color('black')
    t.circle(i)
    t.right(2)
    t.forward(2)

'''
d1={'A':2,'d':3,'E':4}
nd={}
for i,j in d1.items():
    nd[j]=i
print(nd)

def thar(i):
    d1={}
    temp=i
    while(i>0):
        dig=i%10
        l=[]
        for j in range(1,dig+1):
            if(dig%j==0):
                l.append(j)
        d1[dig]=l
        l=[]
        i//=10
    return d1 
num=[1923,1924]
List=[]
for i in num:
    List.append(thar(i))
D=dict(zip(num,List))
print(D)

a=int(input('Enter a number:'))
temp=a
sum=0
while(temp>0):
    dig=temp%10
    if(dig%2==0):
        sum+=dig
    temp//=10
print(sum)

def even(n):
    s=0
    l=int(n)
    for i in range(0,len(n)+1):
        if(i%2==0):
            s=s+int(i)
    return(s)
a=input('Enter the number:')
print('The sum of even digits of ',a,'is',even(a))


a=input('ENter elements with a space between:')
L=[int(i) for i in a.split()]
l=L.copy()
posi=1
for i in l:
    l1=[]
    for j in range(1,i+1):
        if(i%j==0):
            l1.append(j)
    L.insert(posi,l1)
    posi+=2
print(L)



a=input('ENter elements with a space between:')
t=(int(x) for x in a.split())
t1=();t2=();c=()
for i in t:
    for j in range(1,i+1):
        if(i%j==0):
            fact=0
            for k in range(1,j+1):
                if(j%k==0):
                    fact+=1
            if(fact==2):
                t1=t1+(j,)
    t2=t2+(t1,)
    c=c+((i,)+(t1,))
    t1=()
print(t2)
print(c)
'''