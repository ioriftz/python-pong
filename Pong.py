# based on @TokyoEdTech, but with some modifications that I would do

import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# controller 
def createController(xPos, yPos):
    controller = turtle.Turtle()
    controller.speed(0)
    controller.shape("square")
    controller.color("white")
    controller.penup()
    controller.goto(xPos, yPos)

controllerA = createController(-350, 0)
controllerB = createController(350, 0)

# loop
while True:
    window.update()