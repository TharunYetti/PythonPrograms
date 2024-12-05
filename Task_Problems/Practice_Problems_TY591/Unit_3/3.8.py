print("----------FIRST AND LAST DIGITS OF GIVEN NUMBER-----------")
num=int(input("number"))
temp=num
if(num>0):
	x=num%10
rev=0
while(num>0):
	dig=num%10
	rev=rev*10+dig
	num=num//10
if(temp>0):
	y=rev%10
print("First digit of the given number is {} and the last digit is {}".format(y,x))
