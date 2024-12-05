a=[1,"as",34]
print(a[0])
print(a[-3])
b=[1,3,"e","rrrr","=",[1,2,3,4]]
print(b[5][3])
k="RGUKT"
print(k[1])


name=list(input("Enter name in caps:"))
for i in range(len(name)):
    for j in range(i+1):
        print(name[j],end=" ")
    print()
'''n=input("enter a number:")
print("number of digits are",len(n))'''

n1=[1,2,3,4,5]
n2=[6,7,8,9,10]
n1=n1+n2
print(n1)
print(n2*2)
print(n1[1:3])
print(n1[3:])
print(n1[:5])
n1[1:3]="jj",a
print(n1)

k=['a','e','e']
k.insert(1,'THARUN')
print(k)
k.remove('e')
print(k)
del k[0]
print(k)