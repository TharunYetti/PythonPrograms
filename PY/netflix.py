import turtle as t
t.hideturtle()
t.bgcolor('black')
t.speed(5)
t.fillcolor('red')
t.begin_fill()
t.right(90)
t.forward(200)
t.left(90)
t.forward(50)
t.left(90)
t.forward(200)
t.left(90)
t.forward(50)
t.end_fill()
t.penup()
t.goto(140,-200)
t.right(180)
t.pendown()
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(200)
t.left(90)
t.forward(50)
t.left(90)
t.forward(200)
t.end_fill()
t.penup()
t.goto(0,0)
t.pendown()
t.begin_fill()
t.goto(140,-200)
t.left(90)
t.forward(50)
t.left(125)
t.forward(245)
t.left(55)
t.forward(50)
t.end_fill()

t.penup()
for i in range(100):
    t.left(1)
    t.forward(1)


'''
t.left(125)
t.forward(240)
t.left(55)
t.forward(50)
t.left(90)
t.forward(200)
t.left(90)
t.forward(50)
t.left(90)
t.forward(130)
t.right(145)
t.forward(155)
t.left(55)
t.goto(0,0)
t.end_fill()

t.pencolor('green')

'''