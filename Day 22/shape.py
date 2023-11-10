'''
def add(a,b):
    return a+b
print(add(2,3))
print(add(4,5))

def complexop(a,b,c):
    return a+b*c
print(complexop(3,4,5))
print(complexop(7,10,2))

def rnrneks(a):
    for i in range(1,10):
        print(a*i)
rnrneks(2)
'''

# <함수>
def drawsquare(x,y,length):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(1,5):
        t.forward(length)
        t.left(90)

def drawtriangle(x,y,length):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(1,4):
        t.forward(length)
        t.left(120)
    t.home

def drawoctagon(x,y,length):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(1,6):
        t.forward(length)
        t.left(72)

def drawten(x,y,length):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(1,11):
        t.forward(length)
        t.left(36)

def drawcircle(x,y,length):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(1,361):
        t.forward(length)
        t.left(1)

import turtle as t
t.speed(0)
t.shape("turtle")
t.pensize(5)
t.color

# <코드>
# for i in range(1,101):
#     t.forward(100)
#     t.right(5)

# drawsquare(100)
# drawsquare(50)
# drawsquare(10)

# drawtriangle(100)
# drawtriangle(50)
# drawtriangle(10)

# drawoctagon(100)
# drawoctagon(50)
# drawoctagon(10)

# drawten(100)
# drawten(50)
# drawten(10)

# drawcircle(3)
# drawcircle(2)
# drawcircle(1)

drawtriangle(-550,100,400)
drawtriangle(350,150,200)
drawtriangle(-250,-125,100)
drawtriangle(250,-125,250)
t.clear()

drawsquare(-550,100,400)
drawsquare(350,150,200)
drawsquare(-250,-125,100)
drawsquare(250,-125,250)
t.clear()

drawoctagon(-550,100,400)
drawoctagon(350,150,200)
drawoctagon(-250,-125,100)
drawoctagon(250,-300,250)
t.clear()

drawten(-550,100,100)
drawten(350,150,50)
drawten(-250,-125,20)
drawten(250,-300,80)
t.clear()

drawcircle(-550,100,3)
drawcircle(350,150,1.5)
drawcircle(-250,-125,0.5)
drawcircle(250,-300,2)

t.mainloop()