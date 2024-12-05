
'''print("---------STRONG NUMBER------------")
n=int(input('Enter A number:'))
k=n
sum=0
while(n>0):
    digit=n%10
    fact=1
    for i in range(digit,0,-1):
        fact=fact*i
    sum=sum+fact
    n//=10
if(sum==k):
    print("it is a strong number")
else:
    print("it is not a strong number")'''
print("--------ARMSTRONG NUMBER----------")
n=int(input("Enter A Number:"))
x=n
sum=0
while(n>0):
    digit=n%10
    sum=sum+digit**3
    n=n//10
if(sum==x):
    print("given number is an armstrong number")
else:
    print("given number is not an armstrong number")
'''print("--------PRINTING A TO Z ALPHABETS-----------")
i=92
while(i<=122):
    print(chr(i),end="")
    i+=1
print()
print("----------FIRST AND LAST DIGITS OF GIVEN NUMBER-----------")
n=int(input("number"))
z=n
d=0
if(n>0):
	x=n%10
while(n>0):
	z=n%10
	d=d*10+z
	n=n//10
if(d>0):
	y=d%10
print("First digit of the given number is {} and the last digit is {}".format(y,x))
print("----------PALINDROME-----------")
n=int(input("Enter A number: "))
x=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(rev==x):
    print("Entered NUmber is a Palindrome")
else:
    print("It is not a Palindrome")
print("--------PERFECT NUMBERS BETWEEN THE RANGE---------")
n=int(input("Enter a number"))
for i in range(1,n+1):
    k=i**(0.5)
    if(k in range(1,n+1)):
        print(i,end=" ")
print("--------PRIME OR NOT--------")
n=int(input("Enter a number"))
fact=0
for i in range(1,n+1):
    if(n%i==0):
        fact+=1
if(fact==2):
    print("The given number is a prime number")
else:
    print("The given number is not a prime number")'''