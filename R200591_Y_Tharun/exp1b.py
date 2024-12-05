import cmath as cm
a=float(input("Enter the Coefficient of second degree variable:"))
b=float(input("Enter the Coefficient of first degree variable:"))
c=float(input("Enter the constant:"))
disc=(b**2-4*a*c)
root1=(-b+(cm.sqrt(disc)))/(2*a)
root2=(-b-(cm.sqrt(disc)))/(2*a)
if(disc>0):
    print("Roots are real and distinct")
    print("Root1={:.2f} \nRoot2={:.2f}".format(root1.real,root2.real))
elif(disc==0):
    print("The Roots are real and same")
    print("Root1 = Root2 = {:.2f}".format(root1.real))
else:
    print("The Roots are imaginary")
    print("Root1={:.2f}\nRoot2={:.2f}".format(root1,root2))
