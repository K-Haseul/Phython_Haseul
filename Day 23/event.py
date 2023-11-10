import turtle as t
t.speed(0)
t.shape("turtle")
t.pensize(10)
t.color

# <함수>
def colorchangepress(x,y):
    t.color("skyblue")

def colorchangerelease(x,y):
    t.color("black")

def colorclear(x,y):
    t.clear()

def ttj(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

# <실행>
t.onclick(colorchangepress)
t.onclick(colorclear,3)
t.onrelease(colorchangerelease)
t.ondrag(t.goto)
t.onscreenclick(ttj)


t.mainloop()