print("Simple and Compund Interest")
P=float(input('Enter the Total amount Given: '))
T=float(input('Enter the no.of Years of Time: '))
R=float(input('Enter the Rate: '))
print('The Simple Interest')
simple=(P*T*R)/100
print('The simple interest is:',simple)
print('The Compound interest')
frac=R/100
brac=1+frac
pow=brac**T
compound=P*pow
print('The Compound Interest is:',compound)
