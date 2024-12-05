print("-----FIRST PROBLEM-----")
x=int(input("Enter any number"))
y=int(input("Enter another number"))
print("x is {} and y is {}".format(x,y))
print("NOW I WILL SWAP THE TWO TWO NUMBERS YOU HAVE ENTERED")
x,y=y,x
print("x is {} and y is {}".format(x,y))
print("-----SECOND PROBLEM-----")
lth=int(input("Enter the length of the rectangle :"))
brth=int(input("Enter the breadth of the rectangle :"))
peri=2*(lth+brth)
print("Perimeter iof rectangle is",peri)
print("-----THIRD PROBLEM-----")
l=int(input("Enter the length of the rectangle :"))
b=int(input("Enter the breadth of the rectangle :"))
a=l*b
print("Area of the rectangle is {}".format(a))
print("--------FIFTH PROBLEM--------")
le=float(input('Enter lenth in centimeters'))
met=le/100
print("etered lenth in meters is",met)
kilmet=met/1000
print("etered lenth in kilometers is",kilmet)
print("--------SIXTH PROBLEM--------")
celcius=float(input('enter temp. in celcius'))
d=9/5*celcius
F=d+32
print("temp. in forenheat is",F)
print("--------SEVENTH PROBLEM--------")
p,q=int(input("entyer firdt angle")),int(input("entyer second angle"))
r=180-(p+q)
print("Thord angle is ", r)
pri=float(input("enter principel amount"))
time=float(input("enter the time in months"))
rate=float(input("enter the interest rate"))
print("SI is",(pri*time*rate)/100)
pri=float(input("enter principel amount"))
t=float(input("enter the time in months"))
rate=float(input("enter the interest rate"))
ll=rate/100
k=1+ll
#n=float(input("enter the no.of times interest applied per time peroid"))
pp=k**t
ci=pri*pp
print("final amount is %.2f"%ci)
print("THEN,compund interest is %.2f"%(ci-pri))
