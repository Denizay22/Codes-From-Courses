import turtle
import pandas

screen = turtle.Screen()
states_img = "blank_states_img.gif"
screen.addshape(states_img)
turtle.shape(states_img)

states_data = pandas.read_csv("50_states.csv")
state_names = states_data["state"].tolist()

text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
guessed_count = 0
while guessed_count < 50:
    player_answer = screen.textinput(title="??", prompt=f"Guess state. {guessed_count}/50").title()
    if player_answer == "Exit":
        break
    if player_answer in state_names:
        guessed_count += 1
        coords = states_data[states_data["state"] == player_answer]
        print(coords)
        text_turtle.setposition(int(coords["x"]), int(coords["y"]))
        text_turtle.write(f"{player_answer}")
        state_names.remove(player_answer)

print(state_names)
states_to_learn_x = []
states_to_learn_y = []
for state in state_names:
    states_to_learn_x.append(int(states_data[states_data.state == state].x))
    states_to_learn_y.append(int(states_data[states_data.state == state].y))
print(states_to_learn_x)
states_to_learn_dict = {
    "state": state_names,
    "x": states_to_learn_x,
    "y": states_to_learn_y
}
states_to_learn = pandas.DataFrame(states_to_learn_dict)
states_to_learn.to_csv("states_to_learn.csv")
screen.exitonclick()
