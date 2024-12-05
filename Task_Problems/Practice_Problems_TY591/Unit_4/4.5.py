n=input("Enter:")
alphasum=0
chrsum=0
num=0
for i in n:
	if( ( i>chr(64) and i<chr(91) ) or ( i>chr(96) and i<chr(123)) ):
		alphasum+=1
	if( i>chr(32) and i<chr(48) or i>chr(57) and i<chr(65) or i>chr(90) and i<chr(97) or i>chr(122) and i<chr(127) ):
		chrsum+=1
	if(i in range(10)):
		if(i>=0 and i<=9):
			num+=1
print("No.of Alphabets are",alphasum)
print("No.of pecial chracters are",chrsum)
print("No.of Numbers are",num)
