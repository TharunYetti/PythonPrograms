print("------------DAIMOND SHAPE-----------")
n=int(input('ENter how many upper rows do you want:'))
for i in range(n+1):
    print(" "*((n)-i),"* "*i,end="")
    print()
for i in range((n)):
    print(" "*(i+1),"* "*((n-1)-i),end="")
    print()
