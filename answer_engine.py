import pandas
import turtle

data = pandas.read_csv("50_states.csv")

states =data["state"].to_list()

states_coor = dict(zip(data["state"], map(list, zip(map(int, data["x"]), map(int, data["y"])))))

class CheckAnswer:

    def __init__(self,answer):
        self.score = 0
        self.state_x = 0
        self.state_y = 0
        self.player_answer = answer


    def review_answer(self):
        if self.player_answer in states:
            self.score += 1
            self.state_x = states_coor[self.player_answer][0]
            self.state_y = states_coor[self.player_answer][1]

    def draw_answer(self):
        lapiz = turtle.Turtle()
        lapiz.penup()
        lapiz.ht()
        lapiz.goto(self.state_x,self.state_y)
        lapiz.write(f"{self.player_answer}", align="left",font=('Arial', 8, 'normal'))









