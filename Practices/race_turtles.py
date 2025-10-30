# NH 2nd Turtle Racing
#Import all the libraries
import turtle as t
import random as r

# Make and set size of screen
screen=t.Screen()
screen.setup(1200, 1000)

# Make the turtles
Michelangelo = t.Turtle()
Michelangelo.shape("turtle")
Raphael = t.Turtle()
Raphael.shape("turtle")
Donetello = t.Turtle()
Donetello.shape("turtle")
Leonardo = t.Turtle()
Leonardo.shape("turtle")
That_One_Guy = t.Turtle()
That_One_Guy.shape("turtle")

# Make colors for the turtles
Raphael.color("#FF0000")
Michelangelo.color("#FF8800")
Donetello.color("#8400FF")
Leonardo.color("#003CFF")
That_One_Guy.color("#EEFF00")

# Make the finish line
Flag_Guy = t.Turtle()
Flag_Guy.penup()
Flag_Guy.goto(300, 250)
Flag_Guy.pendown()
Flag_Guy.right(90)
Flag_Guy.pensize(10)
Flag_Guy.forward(300)

# Move turtles to starting positions
Raphael.penup()
Raphael.goto(-200, 0)
Raphael.pendown()
Michelangelo.penup()
Michelangelo.goto(-200, 50)
Michelangelo.pendown()
That_One_Guy.penup()
That_One_Guy.goto(-200, 100)
That_One_Guy.pendown()
Leonardo.penup()
Leonardo.goto(-200, 150)
Leonardo.pendown()
Donetello.penup()
Donetello.goto(-200, 200)
Donetello.pendown()

# Make win sentence guy
Win_Guy = t.Turtle()
Win_Guy.penup()
Win_Guy.goto(-200, -200)
# Set speed and movement of turtles & Anounce Winner
turtles = [Raphael, Donetello, Michelangelo, Leonardo, That_One_Guy]
while True:
    for i in turtles:
        if i.xcor() >= 300:
            Win_Guy.pendown()
            Win_Guy.write("We have a winner!!", font = ("Arial", 20, "normal"))
            break
        i.forward(r.randint(1, 25))
        if i.xcor() >= 300:
            Win_Guy.pendown()
            Win_Guy.write("We have a winner!!", font = ("Arial", 20, "normal"))
            break

t.done()