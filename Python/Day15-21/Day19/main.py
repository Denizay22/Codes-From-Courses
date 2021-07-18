from turtle import Turtle, Screen
import random as r

screen = Screen()
# def move_forward():
#     timmy.forward(10)
#
#
# def turn_left():
#     timmy.left(5)
#
#
# def turn_right():
#     timmy.right(5)
#
#
# timmy = Turtle()
# timmy.shape("turtle")
# screen = Screen()
#
# screen.listen()
# screen.onkeypress(move_forward, "w") # onkey does not work for pressing down button.
# screen.onkeypress(turn_left, "a")
# screen.onkeypress(turn_right, "d")
# screen.onkey(timmy.clear, "c")

# --------------------------------------------------------------------------------
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Race", prompt="Which turtle you think win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
for t in range(6):
    new_turtle = Turtle(shape="turtle")
    turtles.append(new_turtle)
    new_turtle.color(colors[t])
    new_turtle.penup()
    new_turtle.setposition(x=-235, y=-80 + t * 30)

race_finished = False
winner_color = ""
while user_choice and not race_finished:
    for t in turtles:
        if t.xcor() >= 230:
            race_finished = True
            winner_color = t.pencolor()
        t.forward(r.randint(0, 10))

if winner_color == user_choice:
    print(f"You've won! The {winner_color} turtle is the winner!")
else:
    print(f"You've lost! The {winner_color} turtle is the winner!")

screen.exitonclick()
