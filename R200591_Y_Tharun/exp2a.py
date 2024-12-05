print("Experiment-2 First task")
start=int(input("Enter starting value:"))
end=int(input("Enter ending value:"))
print("The Even Numbers are ",end=":")
for i in range(start,end+1):
    if(i%2==0):
        if(i==end or i==end-1):
            print(i)
        else:
            print(i,end=",")
