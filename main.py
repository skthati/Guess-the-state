import pandas
import random
from turtle import Turtle, Screen

# Using pandas read csv file.
data = pandas.read_csv("50_states.csv")
# d1 = data[data["state"] == "Texas"]
# if d1.x == -38:
#     print("Weldone!")


# Instance of Turle and Screen Class.
# t = Turtle

s = Screen()

# Global variable declaration
game_state = True
count = 0

# Background image of USA
s.bgpic("blank_states_img.gif")
# s.register_shape("blank_states_img.gif")
# t.shape("blank_states_img.gif")
# Title of window.
s.title("Welcome to State Guess Game!")

while game_state:
    # Text input.
    user_input = s.textinput(f"{count}/50 States Correct", "Guess the state: ")
    # print(user_input)

    # Pull State Series and convert to List.
    row_in_data = data["state"].to_list()
    row_lst = data[data["state"] == user_input]
    # print(str(row_lst.state))
    if row_lst.state.item() == user_input:
        count += 1
        t = Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(row_lst.x), int(row_lst.y))
        t.pendown()
        t.write(row_lst.state.item())
        # t.write(user_input)
    # row_lst = list(row_lst)
    # print(row_lst)








s.mainloop()

