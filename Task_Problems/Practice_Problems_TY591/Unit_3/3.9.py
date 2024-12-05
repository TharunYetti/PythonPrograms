num=int(input("Enter a number to check whether it is a palindrome or not: "))
x=num #assigning the entered number  to a new variable
rev=0
while(num>0):
    digit=num%10
    rev=rev*10+digit
    num//=10
if(rev==x):
    print("Entered number is a palindrome number.")
else:
    print("Entered number is not a palindrome number.")
