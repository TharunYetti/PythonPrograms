sum=0
with open('num.txt','r') as f:
	for i in f:
		sum+=int(i)
	print('The sum is',sum)
print(f)
f.close()
