print("Discount Problem")
quantity=int(input('Enter The No.of Items Purchased'))
cost=quantity*100
discount=cost/10
payable=cost-discount
if(cost>1000):
	print('The Final Cost is:',payable)
else:
	print('The Final Cost is:',cost)	 
