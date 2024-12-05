import cmath
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
def quadratic(a,b,c):
	delta=b**2-4*a*c
	root1=(-b+cmath.sqrt(delta))/(2*a)
	root2=(-b-cmath.sqrt(delta))/(2*a) 
	if(delta>0):
		print("The Roots are Real and distinct")
		print("Root1 =",root1)
		print("Root2 =",root2)
	elif(delta==0):
		print("The Roots are Real and Equal")
		print("Root1 = Root2 =",root1)
	elif(delta<0):
		print("The Roots are Imaginary")
		print("Root1 =",root1.real,"+",round(root1.imag,2),"j")
		print("Root2 =",root2.real,round(root2.imag,2),"j")
root=quadratic(a,b,c)			
if(a!=0):
	print(root)							
else:
	print("The Given Equation is not a quadratic Equation")	
