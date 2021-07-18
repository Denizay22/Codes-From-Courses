import random
import turtle

import colorgram
from turtle import Turtle
from turtle import Screen

timmy = Turtle()
timmy.shape("turtle")
# for _ in range(4):
#    timmy.forward(100)
#    timmy.right(90)


# ---------------------
# dashed line
# for _ in range(50):
#    timmy.forward(10)
#    timmy.penup()
#    timmy.forward(10)
#    timmy.pendown()

# ---------------------
# draw triangle to decagon shapes
#
# for i in range(3, 11):
#     for j in range(i):
#         timmy.forward(100)
#         timmy.right(360 / i)

# ----------------------
# draw a random walk
# timmy.width(10)
# timmy.speed("fastest")
# for _ in range(100):
#     timmy.color(random.random(), random.random(), random.random())
#     timmy.forward(50)
#     timmy.right(random.randint(0, 3) * 90)

# ----------------------
#tuple = finalized list? not changeable
# timmy.speed("fastest")
# timmy.pensize(2)
# for _ in range(int(360/3)):
#     timmy.color(random.random(), random.random(), random.random())
#     timmy.circle(200)
#     timmy.right(3)

# -----------------------
# million dollar painting
# colorsObjects = colorgram.extract("hedgehog.jpg", 100)
# colorRGBs = []
# for color in colorsObjects:
#     rgb = color.rgb
#     colorRGBs.append((rgb.r, rgb.g, rgb.b))
# timmy.penup()
# timmy.speed("fastest")
# timmy.setposition(-300, -300)
# timmy.hideturtle()
# turtle.colormode(255)
# for i in range(10):
#     for _ in range(10):
#         timmy.dot(20, random.choice(colorRGBs))
#         timmy.forward(50)
#     timmy.setposition(-300, -300 + (i + 1) * 50)

window = Screen()
window.exitonclick()

