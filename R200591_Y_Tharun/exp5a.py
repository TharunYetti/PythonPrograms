string1=input('Enter The First String:')
string2=input('Enter The Second String:')
stry1=''
stry2=''
for i in string1:
	if(i.isalpha()):
		stry1+=i
for i in string2:
	if(i.isalpha()):
		stry2+=i
s1=stry1.lower()
s2=stry2.lower()
if(len(s1)==len(s2)):
	for i in s1:
		c1=s1.count(i)
		c2=s2.count(i)
		if(c1!=c2):
			print('The First and Second strings are not Anagrams')
			break
	else:
		print('The First and Second strings are Anagrams')
else:
	print('The First and Second strings are not Anagrams')
	
	
