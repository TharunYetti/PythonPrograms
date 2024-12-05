#file copying
f=open('num.txt','r')
k=f.read(10)
f.close()

#to file
af=open('num2.txt','w')
af.write(k)
af.close()
