s=int(input("Enter starting number:"))
e=int(input("Enter an ending value:"))
for j in range(s,e+1):
    fact=0
    for i in range(1,j+1):
        if(j%i==0):
            fact+=1
    if(fact==2):
        print(i,end=" ")
