
l=int(input("Enter the length of the rectangle :"))
b=int(input("Enter the breadth of the rectangle :"))
t=input("enter 'a' to know the area of rectangle :")
a=l*b
if (t=='a' or t=='A'):
    print("The area of givenp rectangle is",a)
else:
    print("Oops! You have entered the wrong one")
    print("Enter 'a' to know the rectangle")
    
    
u=float(input("enter any number"))
v=float(input("enter another number"))
if (v==0):
	print("print other number other than zero")
i=input("Enter Y to see all arithmetic operatios for above two numbers")
plus=u+v
minus=u-v
div=u/v
mult=u*v
power=u**v
if(i=='Y' or i=='y'):
    print("addition of numbers is",plus)
    print("subtraction of numbers is",minus)
    print("division of numbers is",div)
    print("product of numbers is",mult)
    print("first number power second number is",power)
else:
    print("oops! You have entered the wrong one")
    print("Enter 'Y' to see arithmetic operations")
