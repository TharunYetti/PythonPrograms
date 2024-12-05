print("--------ARMSTRONG NUMBER----------")
n=int(input("Enter A Number:"))
x=n
y=x
ndig=0
while(n>0):
	ndig+=1
	n//=10
print("No of digits are",ndig)
sum=0
while(x>0):
    dig=x%10
    sum=sum+(dig**(ndig))
    x=x//10
if(sum==y):
    print("Given number is an armstrong number")
else:
    print("Given number is not an armstrong number")
