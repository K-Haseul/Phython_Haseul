import turtle as t

score=0
s=t.Screen() 
# s.bgcolor("slategray")
s.screensize(800,800,"slategray")

board=t.Turtle()
board.speed(0)
board.penup()
board.color("white")
board.goto(-150,350)
board.write(f"score:{score}",font=("arial",20,"bold"))
board.hideturtle()

ball=t.Turtle()
ball.speed(0)
ball.penup()
ball.color("white")
ball.shape("circle")
ball.shapesize(1,1)

bar=t.Turtle()
bar.speed(0)
bar.penup()
bar.color("white")
bar.shape("square")
bar.goto(0,-20)
bar.shapesize(1,6)

def gogo():
    if bar.xcor()<20:
        bar.forward(50)

def go():
    if bar.xcor()>-20:
        bar.backward(50)

s.onkeypress(go,"a")
s.onkeypress(gogo,"d")


def gs():
    ballx=10
    bally=7
    score=0
    board.clear()
    board.write("score:0",font=("arial",20,"bold"))
    while True:
        ball.setx(ball.xcor()+ballx)
        ball.sety(ball.ycor()+bally)

        if ball.xcor()>20:
            ballx*=-1
        if ball.ycor()>20:
            bally*=-1
        if ball.xcor()<-20:
            ballx*=-1
        if ball.ycor()<-20:
            board.clear()
            board.write(f"GAME OVER",font=("arial",20,"bold"))
            break
        if (bar.xcor()-50<ball.xcor()<bar.xcor()+50)and(bar.ycor()-10<ball.ycor()<bar.ycor()+10):
            bally*=-1
            score+=1
            board.clear()
            board.write(f"score:{score}",font=("arial",20,"bold"))

s.onkeypress(gs,"s")

s.listen()

s.mainloop()