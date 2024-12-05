n=input("Enter:")
alphasum=0
chrsum=0
num=0
for i in n:
	if( (i>='A' and i<='Z') or (i>='a' and i<='z') ):
		alphasum+=1
	elif(i>='0' and i<='9'):
		num+=1
	elif(i==' '):
		continue
	else:
		chrsum+=1
print("No.of Alphabets are",alphasum)
print("No.of pecial chracters are",chrsum)
print("No.of Numbers are",num)

#	if( i>chr(32) and i<chr(48) or i>chr(57) and i<chr(65) or i>chr(90) and i<chr(97) or i>chr(122) and i<chr(127) ):
#		chrsum+=1
