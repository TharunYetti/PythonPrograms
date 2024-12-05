
'''custnum=int(input("Enter you mobile number: "))
units=int(input("Enter no,of units consumed: "))
if(units>=0 and units<=50):
    roc=1.35
    print(20+roc*units,"is the total amount you have to paid")
elif(units>=51 and units<=100):
    roc=2.60
    print(20+roc*units,"is the total amount you have to paid")
elif(units>=101 and units<=200):
    roc=2.85
    print(20+roc*units,"is the total amount you have to paid")
elif(units>=201 and units<=300):
    roc=4.50
    print(20+roc*units,"is the total amount you have to paid")
elif(units>=301 and units<=400):
    roc=5.0
    print(20+roc*units,"is the total amount you have to paid")
elif(units>400):
    roc=5.75
    print(20+roc*units,"is the total amount you have to paid")  
else:
    print("Please Check Your Input.") 


side1=float(input("Enter first side of triangle"))
side2=float(input("Enter second side of triangle"))
side3=float(input("Enter third side of triangle"))
if(side1+side2>side3 or side2+side3>side1 or side1+side3>side2):
    print("Given parameters can form a triangle")
else:
     print("Given parameters cannot form a triangle")
     
     
alpha=input("enter an alphabet")
vowel=['a','e','i','o','u','A','E','O','U','I']
if(alpha in vowel):
    print(alpha,"is vowel")
else:
    print(alpha,"is a consonant")
    
    
    
char=input("enter any character")
if(char>="a" and char<="z" or char>="A" and char<="Z"):
    print(char," is an alphabet")
else:
    print(char,"is not an aplhabet") 
    
    
       
per1=int(input("First person age: "))
per2=int(input("Second person age: "))
per3=int(input("Third person age: "))
if(per1==per2 or per2==per3 or per1==per3):
    print("Please Enter different ages")
else:
    if(per1>per2 and per1>per3):
        print("person1 is oldest in age")
    elif(per2>per3):
        print("person2 is oldest in age")
    else:
        print("person3 is oldest in age")
    if(per1<per2 and per1<per3):
        print("person1 is youngest in age")
    elif(per2>per3):
        print("person3 is oldest in age")
    else:
        print("person2 is oldest in age")
        
        
        
print("-------MARKS GRADE PROBLEM-------")
m=int(input("Enter your marks: "))
if(m<0 or m>100):
    print("Please Enter correct marks ")
else:
    if(m<25):
        print("Your Grade is F")
    elif(m>=25 and m<45):
        print("Your Grade is E")
    elif(m>=45 and m<50):
        print("Your Grade is D")
    elif(m>=50 and m<60):
        print("Your Grade is C")
    elif(m>=60 and m<80):
        print("Your Grade is B")
    else:
        print("Your Grade is A")
        
        
        
print("-------SALARY BONUS PROBLEM-------")
sal=int(input("Enter your salary"))
exp=int(input("Enter no.of years of experience"))
if(exp>=5):
    print("Your net bonus amount is",sal*(5/100))
else:
    print("You have less than five years pof experience")
    print("So, You dont get any BONUS")
    
    
print("-------First Problem------")
days=int(input("Enter number of Days: "))
years=days//365
weeks=days//7
print("No.of full years are",years)
print("No.of full weeks are",weeks)


print("-------Second Problem------")
b=int(input('b is'))
c=int(input('c is'))
d=int(input('d is'))
total=b+c+d
average=total/3
print("Average marks are %14.3f" %average)


print("-------Third Problem------")
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
num3=int(input("Enter num3: "))
if(num1>=num2 and num1>=num3):
    print(num1,'is the greatest number')
elif(num2>=num3):
    print(num2,'is the greatest number')
else:
        print(num3,"is the greatest number")
        
        
print("-------Fourth Problem------")
fnum=int(input("Enter a number: "))
if(fnum%2==0):
    print(fnum,"is even number")
else:
    print(fnum,"is odd number")
    
    
    
print("-------Fifth Problem------")
year=int(input("Enter a year: "))
if(year%4==0 and year%100!=0):
	print(year,"is leap year")
elif(year%400==0):
	print(year,"is a leap year")    
else:
	print(year,"is not a leap year")

    
print("-------+,-,0 Problem------")
number=float(input("Enter a number"))
if(number>0):
    print(number,"is positive")
elif(number<0):
    print(number,"is negative number")
else:
    print(number,"is a zero")
    
    
print("------ATTENDANCE PROBLEM-------")
print ("Number of classes held")
noh = int(input())
print ("Number of classes attended")
noa = int(input())
atten = (noa/noh)*100
print( "Attendence is %.2f" %atten)
if (atten >= 75):
    print("You are allowed to sit in exam")
else:
    print("Sorry, you are not allowed. Attend more classes from next time.")
    
    
print("------DISCOUNT PROBLEM-------")
print("The value of one packet is 100")
nop=int(input("How many packets do you want : "))
cost=nop*100
discount=cost/10
fcost=cost-discount
if(cost>1000):
    print("Congratulations! You will get discout on your purchase")
    print("The total cost of your purchase is ",fcost)
else:
    print("The total cost of your purchase is ",cost)'''
