import turtle as t
import pandas

CSV_FILENAME = "50_states.csv"
screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)
# create instance of class and set up configs
pen = t.Turtle()
pen.penup()
pen.hideturtle()

# read states file
fifty_states = pandas.read_csv(filepath_or_buffer=CSV_FILENAME)

# this will hold the state names the user has correctly guessed
user_correct_states = []
is_game_on = True

while is_game_on:
    # textinput returns str | None so ensure str conversion to use title()
    answer_state = str(screen.textinput(title="Guess the state", prompt="What's another state name?")).title()

    # end game
    if answer_state == "Exit":
        is_game_on = False

    # select entry that matches user answer
    state_entry = fifty_states[fifty_states["state"] == answer_state]

    # if it is not empty then the DF contains state, x, y
    if not state_entry.empty:
        # grab the coordinate values
        x_coordinate = state_entry.x.iloc[0]
        y_coordinate = state_entry.y.iloc[0]
        pen.setpos(x=x_coordinate, y=y_coordinate)
        pen.write(answer_state)
        user_correct_states.append(answer_state)
        # if the user has guessed all states then game is over
        if len(user_correct_states) == 50:
            is_game_on = False

    


screen.mainloop()
