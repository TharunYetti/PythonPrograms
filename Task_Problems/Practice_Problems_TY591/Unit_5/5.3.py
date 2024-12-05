k='RGUKT'
for i in range(1,len(k)+1):
	for j in range(i):
		print(k[j],end=' ')
	print()
for i in range(len(k)-1,0,-1):
	for j in range(i):
		print(k[j],end=' ')
	print()
