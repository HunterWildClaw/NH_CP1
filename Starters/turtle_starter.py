#NH 2nd turtle warm up

import turtle

def draw_branch(length):
    if length > 5:
        for i in range(3):
            turtle.forward(length)
            draw_branch(length/3)
            turtle.right(180)
            turtle.forward(length)
            turtle.right(60)

turtle.shape("turtle")
turtle.speed(0)
turtle.color("light blue")
turtle.penup()
turtle.goto(0,0)
turtle.pendown()

for i in range(6):
    draw_branch(100)
    turtle.right(60)

turtle.done()