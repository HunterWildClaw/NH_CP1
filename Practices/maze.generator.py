# NH 2nd Maze Generator
# Import random as dum
import random as dum
# Import turtle as bob
import turtle as bob

#Define the rows and collumns
num_rows = 60
num_cols = 60

# Make a function for the maze
def create_maze_grid(rows, cols):
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            block = {
                "visited": False,
                "walls": {
                    "up": True,
                    "down": True,
                    "left": True,
                    "right": True
                }
            }
            row.append(block)
        grid.append(row)
    return grid
cell_size=10
# Make the turtle have infinite speed
bob.speed(1)
bob.tracer(0)
#Hide the turtle after the maze is done
bob.hideturtle()
#Then actually call the function to make the maze
grid=create_maze_grid(num_rows, num_cols)
for i in grid:
    for block in i:
        if block["walls"]["up"]:
            bob.pendown()
            bob.goto(x + cell_size, y)
            bob.penup()
            bob.goto(x, y)
        if block["walls"]["right"]:
            bob.goto(x + cell_size, y)
            bob.pendown()
            bob.goto(x + cell_size, y - cell_size)
            bob.penup()
            bob.goto(x, y)
        if block["walls"]["down"]:
            bob.goto(x + cell_size, y - cell_size)
            bob.pendown()
            bob.goto(x, y - cell_size)
            bob.penup()
            bob.goto(x, y)
        if block["walls"]["left"]:
            bob.goto(x, y - cell_size)
            bob.pendown()
            bob.goto(x, y)
            bob.penup()
        bob.update()
        bob.done()