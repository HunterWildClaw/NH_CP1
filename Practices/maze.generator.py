# NH 2nd Maze Generator
# Import random as dum
import random as dum
# Import turtle as bob
import turtle as bob

# Make a function to test solveabilty of maze
def is_solveable(row_grid, col_grid):
    size = len(row_grid) - 1
    visited = set()
    stack = [(0,0)]

    while stack:
        x, y = stack.pop()

        if x == size - 1 and y ==size - 1:
            return True
        
        if (x, y) in visited:
            continue

        visited.add((x,y))

        if x < size - 1 and col_grid[y][x+1] == 0:
            stack.append((x+1, y))

        if y < size - 1 and row_grid[y+1][x] == 0:
            stack.append((x, y+1))

        if x > 0 and col_grid[x][y] == 0:
            stack.append((x-1, y))

        if y > 0 and row_grid[y][x] == 0:
            stack.append((x, y-1))

    return False


#Make maze generator as a function
def maze_generation():
    #Make the rows
    grid_rows = [[1,1,0,1,1,1],
                 [1,1,1,1,0,1],
                 [1,0,0,1,1,1],
                 [1,1,0,1,0,1],
                 [1,1,0,0,0,1],
                 [1,1,1,0,1,1]]
    for wall in grid_rows:
        if wall == 1:
            bob.pendown()
            bob.forward(100)

        elif wall == 0:
            bob.penup()
            bob.forward(100)

    #Make the collumns
    bob.right(90)
    grid_cols = [[1,1,1,1,1,1],
                 [1,0,0,1,1,1],
                 [1,0,0,1,0,1],
                 [1,0,1,0,1,1],
                 [1,1,0,1,1,1],
                 [1,0,1,1,0,1]]
    for wal in grid_cols:
        if wal == 1:
            bob.pendown()
            bob.forward(100)

        elif wal == 0:
            bob.penup()
            bob.forward(100)

#Make the screen
screen = bob.Screen()
screen.setup(600, 600)

#Make the maze
bob.speed(0)
maze_generation()

bob.done()