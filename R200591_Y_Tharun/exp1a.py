#program to find the simple interest from the user
#first of all taking all inputs from the user
p=int(input("Enter The Principle Amount:"))
t=int(input("Enter The Time in Years:"))
r=int(input("Enter The Rate of Interest:"))
#calculating simple interest with the formula given below and assigning it to a variable 'si'
si=(p*t*r)/100
#now printing the simple interest using .format
print("Simple Interest for the amount {},{} and {} is {}".format(p,t,r,si))

