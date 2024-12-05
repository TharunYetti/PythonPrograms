print("---------String PATTERN------------")
n=input("ENter your name in caps:")
print()
for i in range(len(n)):
    for j in range(i+1):
        print(n[j],end=" ")
    print()
