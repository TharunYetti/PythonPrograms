print("EXPERIMENT-3")
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
        print("Entered is a prime number.")
    else:
        print("Entered is not a prime number.")
print("-------------------------INSTRUCTIONS------------------------------")
print("Enter a number among 1,2,3 and 0, where\n 1 -for finding factorial of that number\n 2 -for checking even numbers in that\n 3 -for checking whether it is a prime or not\n 0 -to stop the execution")
while(True):
    i=int(input("Enter a number among 1,2,3 and 0: "))
    if(i==1):
        num=int(input("Enter any positive number to find its factorial:"))
        fact(num)
    elif(i==2):
        num=int(input("Enter any number to print even digits in that:"))
        evendig(num)
    elif(i==3):
        num=int(input("Enter a number to check whether it is a prime or not:"))
        ifprime(num)
    elif(i==0):
        print("Good Bye!!!")
        break
    else:
        print("Please Enter a Valid Input and Try Again")
