import turtle as t
t.speed(0)
t.shape("turtle")
t.pensize(10)
t.color

def gogo():
    t.forward(30)

def backback():
    t.backward(30)

def turnright():
    t.right(10)


def turnleft():
    t.left(10)

def cclear():
    t.clear()

def colorgreen():
    t.color("green")

def colorblue():
    t.color("blue")

def colorred():
    t.color("red")

def colororange():
    t.color("orange")

def coloryellow():
    t.color("yellow")

def colorwhite():
    t.pensize(20)
    t.color("white")

def turtlemove(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def triangle():
    for i in range(1,4):
        t.forward(100)
        t.left(120)

def square():
    for i in range(1,5):
        t.forward(100)
        t.left(90)

def pentagon():
    for i in range(1,6):
        t.forward(100)
        t.left(72)

def circle():
    t.circle(100)

def circlel():
    t.circle(200)

def circlem():
    t.circle(100)

def circles():
    t.circle(50)

t.onkeypress(gogo,"Up")
t.onkeypress(turnright,"Right")
t.onkeypress(backback,"Down")
t.onkeypress(turnleft,"Left")
t.onkeypress(cclear,"c")
t.onkeypress(colorred,"r")
t.onkeypress(colorgreen,"g")
t.onkeypress(colororange,"o")
t.onkeypress(coloryellow,"y")
t.onkeypress(colorwhite,"w")
t.onscreenclick(turtlemove)
t.onkeypress(triangle,"3")
t.onkeypress(square,"4")
t.onkeypress(pentagon,"5")
t.onkeypress(circle,"0")
t.onkeypress(circlel,"l")
t.onkeypress(circlem,"m")
t.onkeypress(circles,"s")
t.ondrag(t.goto)
t.listen()

t.mainloop()