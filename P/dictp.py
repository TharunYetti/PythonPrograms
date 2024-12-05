'''d={1:'A',2:'K',3:'Y'}
d1={6:'D',5:'E',4:'C'}
key=list(d.keys())+list(d1.keys())
value=list(d.values())+list(d1.values())
nd=dict(zip(key,value))
print(nd)

d={1:'A',2:'K',3:'Y'}
d1={6:'D',5:'E',4:'C'}
d.update(d1)
print(d)'''
#pp1
l1=['A','B','C','D','E']
l2=[1,2,3,4,5]
print(dict(zip(l2,l1)))

#(pp2)
s='hjbuyg2efjekbfufbuifjjbbbffjfjkf j bwkwrwj'
d={x:s.count(x) for x in s}
print(d)
print(d.values())

#(pp4)
l1=[{'maths':23,'Phy':43},{'chem':45,'Eng':34}]
s1='Hll','nvjh'
new=dict(zip(s1,l1))
print(new)
newl=[]
for i in l1:
    sum=0
    for j in i.values():
        sum+=j
    newl.append(sum)
new2=dict(zip(s1,newl))
print(new2)
#pp5
d1={'A':2,'d':3,'E':4}
nd={}
for i,j in d1.items():
    nd[j]=i
print(nd)
#(pp6)
n=10
l={x:x**3 for x in range(1,n) if(x%2==1)}
print(l)
#(pp8)
l=[]
d1={x:x*x for x in range(1,11) if(x%2==0)}
d2={x:x**3 for x in range(1,11) if(x%2==0)}
print(d1,d2)
l1=list(d1.values())
l2=list(d2.values())
for i in range(len(l1)):
    l.append((l1[i],l2[i]))
newdic=dict(zip(d1.keys(),l))
print(newdic)
