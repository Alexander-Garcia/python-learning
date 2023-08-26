import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

user_bet = screen.textinput(title="Place them bets", prompt="Which one will win? Enter a color: ")

for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Ding ding winner. {winning_color} won")
            else:
                print(f"Thanks for the money. Try again. {winning_color} won")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

    

screen.mainloop()
