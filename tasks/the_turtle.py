import turtle
from math import sin, cos, pi

#wohin mit dem pendown, damit keine Linie von (0, 0) nach oben führt
turtle.pendown()

turtle.fillcolor(.5, .1, .9)
turtle.begin_fill()

for i in range(0, 6):
    angle = i * 2 * pi / 5 * 2
    x = 200 * sin(angle)
    y = 200 * cos(angle)
    turtle.goto(x, y)

turtle.end_fill()
input("Waiting for user... press [ENTER] to quit")
