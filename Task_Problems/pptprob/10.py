def words(dig):
	hm=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
	print(hm[int(dig)],end='')
k=input('Enter a number:')
print(k,'is written in words as',end=' ')
for i in k:
	words(i)
print()

'''
def words(dig):
	hm=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
	print(hm[dig],end='')
k=input('Enter a number:')
print(k,'is written in words as',end=' ')
l=[]
while(k>0):
	dig=k%10
	l.append(dig)
	k//=10
l.reverse()
for i in l:
	words(i)
print()

	
'''
