amount=int(input('Enter the Amount:'))
if(amount>=2000):
	amount2000=amount//2000
	amount=amount-amount2000*2000
	print(amount2000,'2000 notes')
if(amount>=500):
	amount500=amount//500
	amount=amount-amount500*500
	print(amount500,'500 notes')
if(amount>=200):
	amount200=amount//200
	amount=amount-amount200*200
	print(amount200,'200 notes')
if(amount>=100):
	amount100=amount//100
	amount=amount-amount100*100
	print(amount100,'100 notes')	
if(amount>=50):
	amount50=amount//50
	amount=amount-amount50*50
	print(amount50,'50 notes')
if(amount>=20):
	amount20=amount//20
	amount=amount-amount20*20
	print(amount20,'20 notes')
if(amount>=10):
	amount10=amount//10
	amount=amount-amount10*10
	print(amount10,'10 notes')	
if(amount<10):
	print(amount,"is the change")	








		
