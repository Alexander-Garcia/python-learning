# working on creating a venv and tables
from prettytable import PrettyTable
from turtle import Turtle, Screen


# using a 3rd party module
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# using a module packaged with Python
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

# task is to draw dashed line
for x in range(10):
    if x % 2 == 0:
        timmy.penup()
        timmy.forward(50)
    else:
        timmy.pd()
        timmy.forward(50)

timmy.reset()

# draw a bunch of shapes on top of each other starting with triangle, square, etc..
sides_drawn = 0
sides_to_draw = 3
for x in range(1, 52):
    timmy.fd(100)
    # use amount of sides to determine angle
    timmy.right(360/sides_to_draw)
    sides_drawn += 1
    if sides_drawn == sides_to_draw:
        sides_drawn = 0
        sides_to_draw += 1

screen = Screen()
screen.exitonclick()
