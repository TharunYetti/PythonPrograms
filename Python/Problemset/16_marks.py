eng=int(input("Enter your english marks:"))
math=int(input("Enter your Maths Marks:"))
phy=int(input("Enter your phy marks:"))
chem=int(input("Enter your chem marks:"))
IT=int(input("Enyer your IT Marks:"))
tot=eng+math+phy+chem+IT
avg=tot/5
ratio=tot/500
percent=ratio*100
print("Your Marks Percentage  in {},{},{},{},{},is:".format('english','maths','physics','chemistry','I T'),percent)

