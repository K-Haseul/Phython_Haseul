import turtle as t

t1=t.Turtle()
t1.shape("turtle")
t1.pensize(5)
t1.speed(0)
t1.color("red")
t1.left(50)
t1.penup()
t1.forward(100)
# t1.pendown()

t2=t.Turtle()
t2.shape("turtle")
t2.pensize(5)
t2.speed(0)
t2.color("green")
t2.right(50)
t2.penup()
t2.forward(100)
# t2.pendown()

t3=t.Turtle()
t3.shape("turtle")
t3.pensize(5)
t3.speed(0)
t3.color("blue")
t3.right(180)
t3.left(50)
t3.penup()
t3.forward(100)
# t3.pendown()

t4=t.Turtle()
t4.shape("turtle")
t4.pensize(5)
t4.speed(0)
t4.color("yellow")
t4.right(180)
t4.right(50)
t4.penup()
t4.forward(100)
# t4.pendown()

t5=t.Turtle()
t5.shape("turtle")
t5.pensize(5)
t5.speed(0)
t5.color("black")
t5.left(90)
t5.penup()

def gogo():
    t1.forward(50)
    t2.forward(50)
    t3.forward(50)
    t4.forward(50)
    t5.forward(50)

def down():
    t1.backward(50)
    t2.backward(50)
    t3.backward(50)
    t4.backward(50)
    t5.backward(50)

def right():
    t1.right(30)
    t2.right(30)
    t3.right(30)
    t4.right(30)
    t5.right(30)

def left():
    t1.left(30)
    t2.left(30)
    t3.left(30)
    t4.left(30)
    t5.left(30)

def same(x,y):
    t1.goto(100,100)
    t2.goto(100,-100)
    t3.goto(-100,-100)
    t4.goto(-100,100)
    t5.goto(0,0)

def dud(x,y):
    t1.goto(0,0)
    t2.goto(0,0)
    t3.goto(0,0)
    t4.goto(0,0)
    t5.goto(0,0)

def penu():
    t1.penup()
    t2.penup()
    t3.penup()
    t4.penup()
    t5.penup()

def pend():
    t1.pendown()
    t2.pendown()
    t3.pendown()
    t4.pendown()
    t5.pendown()

def clear():
    t1.clear()
    t2.clear()
    t3.clear()
    t4.clear()
    t5.clear()

def pen1():
    t1.pensize(1)
    t2.pensize(1)
    t3.pensize(1)
    t4.pensize(1)
    t5.pensize(1)

def pen2():
    t1.pensize(2)
    t2.pensize(2)
    t3.pensize(2)
    t4.pensize(2)
    t5.pensize(2)

def pen3():
    t1.pensize(3)
    t2.pensize(3)
    t3.pensize(3)
    t4.pensize(3)
    t5.pensize(3)

def square():
    t1.shape("square")
    t2.shape("square")
    t3.shape("square")
    t4.shape("square")
    t5.shape("square")

def circle():
    t1.shape("circle")
    t2.shape("circle")
    t3.shape("circle")
    t4.shape("circle")
    t5.shape("circle")

def turtle():
    t1.shape("turtle")
    t2.shape("turtle")
    t3.shape("turtle")
    t4.shape("turtle")
    t5.shape("turtle")

def arrow():
    t1.shape("arrow")
    t2.shape("arrow")
    t3.shape("arrow")
    t4.shape("arrow")
    t5.shape('arrow')

t.onkeypress(gogo,"Up")
t.onkeypress(down,"Down")
t.onkeypress(right,"Right")
t.onkeypress(left,"Left")
t.onscreenclick(same,"1")
t.onscreenclick(dud,"3")
t.onkeypress(gogo,"Up")
t.onkeypress(down,"Down")
t.onkeypress(right,"Right")
t.onkeypress(left,"Left")
t.onkeypress(clear,"c")
t.onkeypress(pen1,"1")
t.onkeypress(pen2,"2")
t.onkeypress(pen3,"3")
t.onkeypress(square,"s")
t.onkeypress(circle,"o")
t.onkeypress(turtle,"t")
t.onkeypress(arrow,"a")



t.listen()
t.mainloop()