import random as r
random_list=['CHATTISGARH','ASSAM','PUNJAB','BIHAR','JARKHAND','MEGHALAYA','RAJASTHAN','TAMILNADU','KARNATAKA','ROSE','JASMINE','SUNFLOWER','LILY','LOTUS','HIBISCUS','MARIGOLD','LAVENDER','CHERRY','COCONUT','DATES','BANANA','APRICOT','APPLE','JACKFRUIT','GUAVA','MANGO','PAPAYA','STRAWBERRY','RRR','YAMADONGA','ROBO','PUSHPA','KHILADI','MAHANATI','AKHANDA','DHRUVA','JULAYI','KRACK','JERSEY','UPPENA','EEGA','MAESTRO','BHEESHMA','JAANU']
name=input('Enter your Name to proceed in Game :')
d={'states':['CHATTISGARH','ASSAM','PUNJAB','BIHAR','JARKHAND','MEGHALAYA','RAJASTHAN','TAMILNADU','KARNATAKA'],'fruits':['CHERRY','COCONUT','DATES','BANANA','APRICOT','APPLE','JACKFRUIT','GUAVA','MANGO','PAPAYA','STRAWBERRY'],'flowers':['ROSE','JASMINE','SUNFLOWER','LILY','LOTUS','HIBISCUS','MARIGOLD','LAVENDER'],'movies':['RRR','YAMADONGA','ROBO','PUSHPA','KHILADI','MAHANATI','AKHANDA','DHRUVA','JULAYI','KRACK','JERSEY','UPPENA','EEGA','MAESTRO','BHEESHMA','JAANU']}
print('<<<<<<<<<<<----------------------- GUESS_THE_WORD_GAME RULES---------------------------->>>>>>>>>>>>'.center(150),'\b1.For Entering the every correct letter you will get +10 marks\n2.For every wrong letter entered you will get -5 marks\n3.You have to enter only in Caps\n4.If the word contains a letter more then one time then you will get only 10 marks becuse marks are for letters.\n5.CAPSLOCK should be on\n6.I made my AI to select only single words,So please try only single words letters otherwise you will loose your marks\n7.If you want to stop the code,enter (ctrl+c)\n','<<<<<<<<<<<----------------------- GUESS_THE_WORD_GAME ---------------------------->>>>>>>>>>>>'.center(149))
print('Ok \'{}\' Now find the random word that my AI selected'.format(name))
item=r.choice(random_list);li=list(item);P=0
if(item in d['states']):
	print('HINT: Inidan States')
elif(item in d['fruits']):
	print('HINT: Indian Fruits')
elif(item in d['flowers']):
	print('HINT: Indian Flowers')
elif(item in d['movies']):
	print('HINT: Tollywood Movies')
find=['_' for x in range(len(li))]
stry=''
for i in find:
	stry+=i
print(*find,sep=' ')
while(True):
	inp=input('>>>>> Enter one letter in selected word:')
	if(inp in item):
		if(inp not in find):
			P+=10
		for i in item:
		        if(inp==i):
		                v=0
		                for k in range(item.count(inp)):
		                	find.pop(li.index(i,v))
		                	find.insert(li.index(inp,v),inp)
		                	v=li.index(i,v)+1
		print(*find,sep=' ')
		print('>>>>> Correct! Now select Another Letter\t\t\t\t\t\t\t\tPOINTS:{}'.format(P))
	else:
	        P-=5
	        print('>>>>> Sorry! \'{}\' not in the Seletced Word\t\t\t\t\t\t\t\tPOINTS:{}'.format(inp,P))
	if('_' not in find):
		print('CONGRATULATIONS!!!!!! YOU FOUND IT\t\t\t\t\t\t\t\t\tTOTAL :{}'.format(P))
		break
f=open('Game_marks.txt','a+')
f.write(name+' : '+str(P)+' Points'+'\n')
f.close()
