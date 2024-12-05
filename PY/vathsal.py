def f(value,values):
    v=1
    values[0]=44
t=3
v=[1,2,3]
f(t,v)
print(t,v[0])
'''
import turtle as t
import colorsys
t=t.Turtle()
s=t.getscreen().bgcolor("black")
t.speed("fast")
n=70
h=0
for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t.color(c)
    t.left(1)
    t.fd(1)
for i in range(10):
    t.left(2)
    t.circle(100)
'''