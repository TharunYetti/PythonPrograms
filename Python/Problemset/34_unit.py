num=input('Enter Your Customer Number: ')
unit=float(input('Enter the No.Of Units Consumed: '))
if(unit<=50):
	print('The Amount to be Paid is: ',(unit*1.35)+20)
elif(unit>=51 and unit<=100):
	print('The Amount to be Paid is: ',(unit*2.60)+20)
elif(unit>=101 and unit<=200):
	print('The Amount To Be Paid is: ',(unit*2.85)+20)
elif(unit>=201 and unit<=300):
	print('The Amount To Be Paid is: ',(unit*4.50)+20)
elif(unit>=301 and unit<=400):
	print('The Amount to be Paid is: ',(unit*5.00)+20)	
elif(unit>=401):
	print('The Amount to be Paid is: ',(unit*5.75)+20)

