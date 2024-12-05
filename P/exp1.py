#finding simple interest with user-input values
p=int(input("Enter Principle Amount: "))
t=int(input("Enter Time in Years: "))
r=int(input("Enter The Rate: "))
si=(p*t*r)/100
if(p<0 or t<0 or r<0):
    print("Please check your values")
else:
    print("simple interest for {},{} and {} is {}".format(p,t,r,si))