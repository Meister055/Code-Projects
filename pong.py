### Setup ###
import turtle as t
import os

playerAscore = 0
playerBscore = 0



### Creating the Window ###
window = t.Screen
t.title("Pong")
t.bgcolor("black")
t.setup(width=800,height=600)
t.tracer(0)

### Left Paddle ###
leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

### Right Paddle ###
rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

### Ball ###
ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(5,5)
ballxdirection = 0.2
ballydirection = 0.2

### Scoreboard ###
pen=t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score",align="center",font=('LCDMono',24,'normal'))

### Left Paddle Movement ###
def leftpaddleup():
    y=leftpaddle.ycor()
    y += 90
    leftpaddle.sety(y)

def leftpaddledown():
    y=leftpaddle.ycor()
    y -= 90
    leftpaddle.sety(y)

### Right Paddle Movement ###
def rightpaddleup():
    y=rightpaddle.ycor()
    y += 90
    rightpaddle.sety(y)

def rightpaddledown():
    y=rightpaddle.ycor()
    y -= 90
    rightpaddle.sety(y)

### Keybinds ###
t.listen()
t.onkeypress(leftpaddleup,'w')
t.onkeypress(leftpaddledown,'s')
t.onkeypress(rightpaddleup,'Up')
t.onkeypress(rightpaddledown,'Down')



### Main Game Loop ###
while playerAscore or playerBscore <= 11:
    t.update()

    # Moving the Ball #
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)

    # Border Setup #
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ballxdirection = ballxdirection * -1
        playerAscore += 1
        pen.clear()
        pen.write(str(playerAscore) + "                    " + str(playerBscore).format(),align="center",font=('LCDMono',24,"normal"))
        os.system("afplay wallhit.wav&")
        
        # Paddle Colisions #
        if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
            ball.setx(340)
            ballxdirection = ballxdirection * -1
            os.system("afplay wallhit.wav&")

        if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
            ball.setx(-340)
            ballxdirection = ballxdirection * -1
            os.system("afplay wallhit.wav&")