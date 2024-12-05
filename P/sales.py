days=int(input('How many days:'))
f=open('sales.txt','w')
for i in range(1,days+1):
	sale=float(input('Enter the sales of day #'+str(i)+':'))
	f.write(str(sale)+'\n')
f.close()
f=open('sales.txt','r')
l=f.readline()
while(l!=''):
	num=float(l)
	print('%.2f'%num)
	l=f.readline()
f.close()
f=open('sales.txt','r')

#printing even sales
for i in f:
	amount=float(i)
	if(int(amount)%2==0):
		print(int(amount))
