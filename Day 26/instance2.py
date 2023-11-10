import turtle as t
s=t.Screen() #배경객체 만들기
class 거북이:
    def __init__(self,color,x,y,pensize):
        self.color=color
        self.x=x
        self.y=y
        self.pensize=pensize
        self.공통점()
        self.차이점()

    def 공통점(self):
        self.객체=t.Turtle()
        self.객체.speed(0)
        self.객체.shape("turtle")
        self.객체.penup()
        self.객체.turtlesize(3)

    def 차이점(self):
        self.객체.goto(self.x,self.y)
        self.객체.color(self.color)
        self.객체.pensize(self.pensize)

t1=거북이("black",0,0,1)
t2=거북이("blue",100,100,2)
t3=거북이("yellow",100,-100,3)
t4=거북이("green",-100,-100,4)
t5=거북이("red",-100,100,5)

    
def gogo():
    t1.객체.forward(50)
    t2.객체.forward(50)
    t3.객체.forward(50)
    t4.객체.forward(50)
    t5.객체.forward(50)

def down():
    t1.객체.backward(50)
    t2.객체.backward(50)
    t3.객체.backward(50)
    t4.객체.backward(50)
    t5.객체.backward(50)

def right():
    t1.객체.right(30)
    t2.객체.right(30)
    t3.객체.right(30)
    t4.객체.right(30)
    t5.객체.right(30)

def left():
    t1.객체.left(30)
    t2.객체.left(30)
    t3.객체.left(30)
    t4.객체.left(30)
    t5.객체.left(30)

def penu():
    t1.객체.penup()
    t2.객체.penup()
    t3.객체.penup()
    t4.객체.penup()
    t5.객체.penup()

def pend():
    t1.객체.pendown()
    t2.객체.pendown()
    t3.객체.pendown()
    t4.객체.pendown()
    t5.객체.pendown()

def clearr(x,y):
    t1.객체.clear()
    t2.객체.clear()
    t3.객체.clear()
    t4.객체.clear()
    t5.객체.clear()

def clearrr():
    t1.객체.clear()
    t2.객체.clear()
    t3.객체.clear()
    t4.객체.clear()
    t5.객체.clear()

def same(x,y):
    t1.goto(100,100)
    t2.goto(100,-100)
    t3.goto(-100,-100)
    t4.goto(-100,100)
    t5.goto(0,0)

s.onkeypress(gogo,"Up")
s.onkeypress(down,"Down")
s.onkeypress(right,"Right")
s.onkeypress(left,"Left")
s.onkeypress(pend,"d")
s.onkeypress(penu,"u")
s.onkeypress(clearrr,"c")
s.onscreenclick(clearr,"1")
s.onkeypress(clearrr,"c")
s.onscreenclick(clearr,"1")
s.onscreenclick(same,"3")

t.listen()





s.mainloop()