import random
import turtle as t

# color = ["blue", "sea green", "red", "olive", "magenta", "coral", "saddle brown"]
direction = [0, 90, 180, 270]
t.colormode(255)
# random_shape = t.Turtle()
# random_walk = t.Turtle()
spirograph = t.Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


spirograph.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        spirograph.color(random_color())
        spirograph.circle(100)
        spirograph.setheading(spirograph.heading() + size_of_gap)


draw_spirograph(5)

# # Drawing shapes from 3 sides till 10 sides
# def draw_shape(no_of_sides):
#     angle = 360 / no_of_sides
#     for __ in range(no_of_sides):
#         random_shape.forward(100)
#         random_shape.right(angle)
#
#
# for no_of_side in range(3, 11):
#     random_shape.color(random_color())
#     draw_shape(no_of_side)
#
# # Random walk
# random_walk.pensize(5)
# random_walk.speed("fastest")
# for _ in range(200):
#     random_walk.color(random_color())
#     random_walk.setheading(random.choice(direction))
#     random_walk.forward(20)
#
# # Dash Line
# for _ in range(4):
#     for __ in range(15):
#         random_shape.forward(10)
#         random_shape.penup()
#         random_shape.forward(10)
#         random_shape.pendown()
#     random_shape.right(90)

screen = t.Screen()
screen.exitonclick()
