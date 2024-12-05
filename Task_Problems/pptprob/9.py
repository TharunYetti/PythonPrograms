def words(text):
	nword=1
	for i in text:
		if(i==' '):
			nword+=1
	print("Total No. of Words in the text:",nword)
text=input("Enter a text to jnow how many words does it contain:")
words(text)
