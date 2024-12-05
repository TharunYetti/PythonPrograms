cost=float(input('Enter the Cost of the Product: '))
sell=float(input('Enter the Selling Price of the Product: '))
if(cost>sell):
	print('The Loss is',cost-sell)
elif(sell>cost):
	print('The Profit is',sell-cost)
else:
	print('No Profit or No Loss')		
