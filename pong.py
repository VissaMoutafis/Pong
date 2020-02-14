#Simple pong game
#By VissaMoutafis
#A game created for educational purposes
#Implemented without classes
#Not my original implementation. I just enchanced it. Enjoy ;)

import turtle  # very basic gui design module
import time
import os

#Window
wn = turtle.Screen()  # we need a screen
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=700, height=500)
wn.tracer(0)

#Choose Multiplayer or Single player
message = turtle.Turtle()
message.speed(0)
message.color("white")
message.penup()
message.hideturtle()
message.write("Pick a Mode!", False, align='center',
              font=('Arial', 15, 'normal'))
answers = {"Singleplayer": 1, "Multiplayer": 2}
answer = wn.textinput(
    "pick a mode: ", "Type one of the following: ".join(answers))

version = ""
if(answer == "Singleplayer"):
    version = "singleplayer"
    print("Entering singleplayer... AI Bot getting ready for first round...")
else:
    version = "multiplayer"
    print("Entering multiplayer")
message.clear()

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 210)

#Paddle A
a_score = 0
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=4, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.hideturtle()

#Paddle B
b_score = 0
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=4, stretch_len=1)
paddle_b.penup()
paddle_b.goto(345, 0)
paddle_b.hideturtle()

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
max_dx = 6
max_dy = 6
ball.dx = 2
ball.dy = 2

#Function for moving a up


def paddle_a_up():
    if(paddle_a.ycor() < 205):
        y = paddle_a.ycor()  # get the y coordinates
        y += 20
        paddle_a.sety(y)  # move the paddle 20px up

#Function for movin a down


def paddle_a_down():
    if(paddle_a.ycor() > -205):
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)


def paddle_b_up():
    if(paddle_b.ycor() < 205):
        y = paddle_b.ycor()  # get the y coordinates
        y += 20
        paddle_b.sety(y)  # move the paddle 20px up

#Function for movin a down


def paddle_b_down():
    if(paddle_b.ycor() > -205):
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)


aiPaddle = paddle_a
ai_down = paddle_a_down
ai_up = paddle_a_up

#AI BOT for singleplayer mode
def ai_paddle_move():
    _y = ball.ycor()
    y = aiPaddle.ycor()

    #if the paddle is higher that the ball and the ball is moving downwards then go down
    if y > _y and ball.dy < 0:
        ai_down()
    elif y < _y and ball.dy > 0:
        ai_up()


#Keyboard listening
wn.listen()
if version == "multiplayer":
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


def updateScore():
    scoreBoard = "Score: A = " + str(a_score) + " - B = " + str(b_score)
    pen.clear()
    pen.write(scoreBoard, align="center", font=("Courier", 20, "bold"))


#Main Loop
paddle_a.showturtle()
paddle_b.showturtle()

while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if(version == "singleplayer"):
        ai_paddle_move()
    updateScore()

    #border checking
    if ball.ycor() > 250:
        ball.sety(250)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if ball.ycor() < -250:
        ball.sety(-250)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if ball.xcor() > 350:
        ball.goto(0, 0)
        ball.dx = -2  # re-initialize the speed
        a_score += 1

    if ball.xcor() < -350:
        ball.goto(0, 0)
        ball.dx = 2  # re-initialize the speed
        b_score += 1

    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350):
        if ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
            ball.setx(335)
            ball.dx *= -1.1  # increase speed each time we hit the ball
            os.system("aplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350):
        if ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
            ball.setx(-335)
            ball.dx *= -1.1  # increase speed each time we hit the ball
            os.system("aplay bounce.wav&")
