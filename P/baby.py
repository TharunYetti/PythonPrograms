li=[2,3,4,5,6,7,8,9]
new=li.copy()
for i in new:
	fact=0
	for j in range(1,i+1):
		if(i%j==0):
            		fact+=1
	if(fact==2):
		li.remove(i)
print(li)
