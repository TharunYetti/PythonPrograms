'''#program to find roots of given quadratic equation
a=float(input("Enter coefficient of second degree variable:"))
b=float(input("Enter coefficient of first degree variable:"))
c=float(input("Enter value of constant:"))
disc=(b**2-4*a*c)
root1=(-b+(disc**(0.5)))/(2*a)
root2=(-b-(disc**(0.5)))/(2*a)
if(disc>0):
	print("Roots are real and distinct\nRoot1={:.2f}\nRoot2={:.2f}".format(root1,root2))
elif(disc==0):
	print("Roots are real and same\nRoot1=Root2={:.2f}".format(root1))
else:
	print("The roots are imagnary\nRoot1={:.2f}\nRoot2={:.2f}".format(root1,root2))'''
print("Experiment-1 First task")
start=int(input("Enter starting value:"))
end=int(input("Enter ending value:"))
print("The Even Numbers are ",end=":")
for i in range(start,end+1):
	if(i%2==0):
		print(i,sep=",")
print()
