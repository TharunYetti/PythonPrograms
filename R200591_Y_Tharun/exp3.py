print("-----------------------------INSTRUCTIONS------------------------------")
print("Here are some navigation numbers, Enter \n 1-to find  the FACTORIAL of a number \n 2-to find the EVEN DIGITS of a number \n 3-to find whether the number is PRIME OR NOT\n 0-to STOP the execution")
def fact(num):
    fact=1
    for j in range(num,0,-1):
        fact=fact*j
    print("Factorial of Enterred Number is",fact)
def evendig(num):
    li=[]
    while(num>0):
        dig=num%10
        if(dig%2==0):
        	if(dig not in li):
                	li.append(dig)
        num=num//10
    li.sort()
    print("The even digits in that number",li)
def ifprime(num):
    fact=0
    for i in range(1,num+1):
        if(num%i==0):
            fact+=1
    if(fact==2):
        print("It is a prime number.")
    else:
        print("It is not a prime number.")
while(1>0):
    i=int(input("Enter a number among 1,2,3 and 0: "))
    if(i==1):
        num=int(input("Enter any number to find its factorial:"))
        fact(num)
    elif(i==2):
        num=int(input("Enter any number to print even digits in that:"))
        evendig(num)
    elif(i==3):
        num=int(input("Enter a number to check whether it is a prime or not:"))
        ifprime(num)
    elif(i==0):
        print("Good Bye!!")
        break
    else:
        print("Please Enter a Valid Input and Try Again")
