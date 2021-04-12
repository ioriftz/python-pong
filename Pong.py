# based on @TokyoEdTech, but with some modifications that I would do

import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# controller definition
class controller(turtle.Turtle):
    def __init__(self, id, xPos, yPos):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xPos, yPos)

# ball definition
class ball(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0,0)

# "instantiate" both controllers
controllerA = controller("1", -350, 0)
controllerB = controller("2", 350, 0)

# "instantiate" the ball
ball = ball()

def move1UP():
    y = controllerA.ycor()
    y += 20
    controllerA.sety(y)

def move1DOWN():
    y = controllerA.ycor()
    y -= 20
    controllerA.sety(y)

def move2UP():
    y = controllerB.ycor()
    y += 20
    controllerB.sety(y)

def move2DOWN():
    y = controllerB.ycor()
    y -= 20
    controllerB.sety(y)

# keyboard binding
window.listen()
window.onkeypress(move1UP, "w")
window.onkeypress(move1DOWN, "s")
window.onkeypress(move2UP, "i")
window.onkeypress(move2DOWN, "k")

# loop
while True:
    window.update()