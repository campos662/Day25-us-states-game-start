import turtle
import pandas

screen = turtle.Screen()
screen.title("US. States Game!!")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
missing_states = []



while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's another State name?").title()
    if answer_state == "Exit":
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        lapiz = turtle.Turtle()
        lapiz.ht()
        lapiz.penup()
        state_data = data[data.state == answer_state]
        lapiz.goto(int(state_data.x), int(state_data.y))
        lapiz.write(answer_state)

for x in all_states:
    if x not in guessed_states:
        missing_states.append(x)

states_to_learn = pandas.DataFrame(missing_states)

states_to_learn.to_csv("states_to_learn.csv")














