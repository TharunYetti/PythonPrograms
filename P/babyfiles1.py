f=open('dummytext.txt','r')
k=f.readlines()
print('No of lines in the file are',len(k))
words=0
letters=0
vowels=0
conson=0
v='aeiouAEIOU'
d={}
words_list=[]
start_letters=[]
for i in k:
	newl=i.split()
	for j in newl:
		words+=1
		words_list.append(j)
	for k in i:
		new2=k.split()
		for m in new2:
			if(m.isalpha()):
				letters+=1
				if(m not in start_letters):
					start_letters.append(m)
			if(m in v):
				vowels+=1
			elif(m.isalpha() and m not in v):
				conson+=1
start_letters.sort()		
for i in start_letters:
	temp=[]
	for j in words_list:
		if(j[0]==i):
			temp.append(j)
	if(temp!=[]):
		d[i]=temp
print('No of words in the file are',words)
print('No of letters in the file are',letters)
print('No of vowels in the file are',vowels)
print('No of consonants in the file are',conson)
print(d)
