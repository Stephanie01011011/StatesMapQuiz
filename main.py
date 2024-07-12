import turtle
import csv
import pandas


state_data = pandas.read_csv("./50_states.csv")
list_of_states = state_data["state"].tolist()
print(list_of_states)


guessed = []
screen = turtle.Screen()
screen.title("U.S States game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

while len(guessed) < 50:
    answer_state = screen.textinput(title=f"Score: {len(guessed)}", prompt="Whats another states name?").title()

    for state in list_of_states:
        if state == answer_state:
            guessed.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            location = state_data[state_data["state"] == state]
            t.goto(int(location["x"]), int(location["y"]))
            t.write(state)
    if answer_state.title() == "Exit":
        break

# states_to_learn.csv
missing_states = []
for state in list_of_states:
    if state not in guessed:
        missing_states.append(state)

new_data = pandas.DataFrame(missing_states)
new_data.to_csv("States_to_learn.csv")
screen.exitonclick()


