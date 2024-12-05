str1=input("Enter any str:")
vowel=['a','e','i','o','u','A','E','I','O','U']
str2=""
for i in str1:
	if(i not in vowel):
		str2+=i
print(str2)

