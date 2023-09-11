# goal of this is to build an etch-A-Sketch type App
# w = forwards
# s = backwards
# a = Counter-clockwise
# d = Clokcwise
# c = Clear drawing
import turtle as t

timmy = t.Turtle()
screen = t.Screen()
# turn on listener
screen.listen()

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def turn_clockwise():
    timmy.right(10)

def turn_counter_clockwise():
    timmy.left(10)

def clear_drawing():
    timmy.reset()

screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_counter_clockwise, key="a")
screen.onkey(fun=turn_clockwise, key="d")
screen.onkey(fun=clear_drawing, key="c")

screen.mainloop()
