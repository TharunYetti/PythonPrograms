print("Experiment-2 Second task")
num=int(input("Input: "))
x=num
rev=0
while(num>0):
    digit=num%10
    rev=rev*10+digit
    num//=10
if(rev==x):
    print("Entered number is a palindrome number.")
else:
    print("Entered number is not a palindrome number.")
