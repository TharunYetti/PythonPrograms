'''i=0
while(i<5):
    j=0
    while(j<5):
        print("*",end=" ")
        j+=1
    print("*")
    i+=1

#(DIAMOND PATTTTTTTTTTTTTEEEEEEEEEEEERRRRRRRNNNNNNNNNNNNN)
for i in range(7):
	print(" "*(6-i),'* '*i,end=" ")
	print()
for j in range(6):
	print(' '*(j+1),'* '*(5-j),end=" ")
	print()

print("-----------fourth-----------")
n1=int(input("Enter First Number"))
n2=int(input("Enter Second Number"))
n3=int(input("Enter Third Number"))
if (n1!=n2 or n2!=n3):
    if(n1>=n2 and n1>=n3):
        print(n1,"is the greatest number")
    elif(n2>n3):
        print(n2,"is the greatest number")
    else:
        print(n3,'is the greatest number')
    if(n1<=n2 and n1<=n3):
        print(n1,"is the lowest number")
    elif(n2<n3):
        print(n2,"is the lowest number")
    else:
        print(n3,'is the lowest number')
else:
    print("all are equal")
    

print("-----------fourth-----------")
alpha={1:'P',2:'Y',3:'T',4:'H',5:'O',6:'N'}
for i in alpha:
    j=1
    while(j<=i):
        print(alpha[j],end=" ")
        j+=1
    print()
    
py=['P','Y','T','H','O','N']
for i in range(len(py)):
	for j in range(i+1):
		print(py[j],end=' ')
	print()
	
	
print("-----------fourth-----------")
n=int(input("Enter A number: "))
for i in range(n):
    for j in range(i):
        print('*',end=" ")
    print()
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=" ")
    print()
print("-----------third-----------")
start=int(input("Enter Start Number: "))
end=int(input("Enter End Number: "))
sum=0
while(start<=end):
    if(start%2==0):
        sum=sum+start    
    elif(start%2!=0):
        while(start+1<=end):
            sum=sum+(start+1)
            start=start+2
    start=start+2
print("sum is",sum)
print("-----------third-----------")
n=int(input("enter a number"))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print("sum is",sum)
print("-----------second-----------")
n=int(input("enter a number"))
s=0
while(n>0):
    s+=1
    n=n//10
print(s)    
print("-----------second-----------")
num=int(input("Enter any Number: "))
sum=0
while(num>0):
    digit=num%10
    sum+=digit
    num=num//10
print(sum)
print("-----------first-----------")
num=int(input("Enter any Number: "))
sum=1
while(num>0):
    digit=num%10
    sum*=digit
    num=num//10
print(sum)'''
