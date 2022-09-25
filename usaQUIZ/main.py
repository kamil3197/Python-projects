import pandas as pd
import turtle

game_is_on = True

#screen config
screen = turtle.Screen()
screen.title("The US QUIZ")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

#states and cords table
data = pd.read_csv("50_states.csv")
states = (data["state"]).to_list()


#turtle config to not see him on the map before writing state's name
tim = turtle.Turtle()
tim.hideturtle()
tim.penup()


# getting cords from guessed state
def getting_cords():
    guessed_state = data.loc[data['state'] == guess]
    x_cor_a = (guessed_state['x'])
    y_cor_b = (guessed_state['y'])
    x_cor = x_cor_a._get_value(0, 'x')
    y_cor = y_cor_b._get_value(0, 'y')
    return x_cor, y_cor

#list for guessed states
guessed_states = []
x = 0

# states not guessed
def states_not_guessed():
    states_to_learn = [element for element in states if element not in guessed_states]
    dict_to_learn = {
        "states": states_to_learn
    }
    print(dict_to_learn)
    new_file = pd.DataFrame(dict_to_learn)
    new_file.to_csv('states_to_learn.csv')

#play the game
while game_is_on:
    bingo = (f"{x}/50 states correct")
    answer_state = screen.textinput(title=bingo, prompt="What's another state's name?").lower()
    guess = answer_state.title()
    if answer_state == "exit":
        states_not_guessed()
        break
    if guess in states and guess not in guessed_states:
        getting_cords()
        x += 1
        guessed_states.append(guess)
        tim.setpos(getting_cords())
        tim.write(guess)
    if x == 50:
        game_is_on = False




screen.exitonclick()
