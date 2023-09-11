import turtle as t
import random
import colorgram

# returns a list of Color objects
colors = colorgram.extract('painting.jpeg', 20)
rgb_colors = []

# turn them into a tuple that Turtle can use. Omit first 4 entries as its just shades of white
for index, color in enumerate(colors):
    if index not in [0, 1, 2, 3]:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)


t.colormode(255)
timmy = t.Turtle()
# hiding speeds up drawing and we don't really need to see Timmy for this
timmy.hideturtle()
# grab screen width and height but give buffer of 10
# these will be used to offset his starting pos(x,y)
starting_x = (timmy.screen.window_width() - 50) / 2
starting_y = (timmy.screen.window_height() - 50) / 2

timmy.penup()
 # starting 0, 0 is center of screen so offset to start bottom left
timmy.setposition(-starting_x, -starting_y)
for x in range(1, 11):
    for y in range(10):
        timmy.pendown()
        timmy.dot(20, random.choice(rgb_colors))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()

    timmy.penup()
    timmy.setposition(-starting_x , -starting_y + (x * 30))

timmy.screen.mainloop()
