inp=input('Enter some strings with a space gap between them:')
final_dict={}
words_list=inp.split()
first_letters=[]
for string in words_list:
	if(string[0] not in first_letters):
		first_letters.append(string[0])
for i in first_letters:
	each_word=()
	for j in words_list:
		if(j[0]==i):
			each_word+=(j,)
	final_dict[i]=each_word
print(final_dict)
			
