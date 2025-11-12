# NH 2nd Maze Generator
# Import random as dum
import random as dum
# Import turtle as bob
import turtle as bob

#Make the screen and screen size
screen=bob.Screen()
screen.setup(999, 1000)

#Make the rows by generating random numbers for whther or not the pen is up or down
def maze_generation():
    #Set it to the right position
    bob.teleport(0,-100)
    # MAKE IT SPEEDY!
    bob.speed(0)
    bob.tracer()
    # Ands makes its faces thes rights directions
    bob.setheading(0)
    #Now generate the rows... one by one. *SIGH*
    row=dum.randint(0,1)
    if row == 0:
        bob.penup()
        bob.forward(100)
    elif row == 1:
        bob.pendown()
        bob.forward(100)
    
    row_1=dum.randint(0,1)
    if row_1==0:
        bob.penup()
        bob.forward(100)
    elif row_1 == 1:
        bob.pendown()
        bob.forward(100)

    row_2=dum.randint(0,1)
    if row_2 == 0:
        bob.penup()
        bob.forward(100)
    elif row_2 == 1:
        bob.pendown()
        bob.forward(100)    

    row_3=dum.randint(0,1)
    if row_3==0:
        bob.penup()
        bob.forward(100)
    elif row_3==1:
        bob.pendown()
        bob.forward(100)

    row_4=dum.randint(0,1)
    if row_4==0:
        bob.penup()
        bob.forward(100)
    elif row_4==1:
        bob.pendown()
        bob.forward(100)

    row_5=dum.randint(0,1)
    if row_5==0:
        bob.penup()
        bob.forward(100)
    elif row_5==1:
        bob.pendown()
        bob.forward(100)

    row_6=dum.randint(0,1)
    bob.teleport(0,-200)
    if row_6==0:
        bob.penup()
        bob.forward(100)
    elif row_6==1:
        bob.pendown()
        bob.forward(100)

    row_7=dum.randint(0,1)
    if row_7==0:
        bob.penup()
        bob.forward(100)
    elif row_7==1:
        bob.pendown()
        bob.forward(100)

    row_8=dum.randint(0,1)
    if row_8==0:
        bob.penup()
        bob.forward(100)
    elif row_8==1:
        bob.pendown()
        bob.forward(100)
    
    row_9=dum.randint(0,1)
    if row_9==0:
        bob.penup()
        bob.forward(100)
    elif row_9==1:
        bob.pendown()
        bob.forward(100)

    row_10=dum.randint(0,1)
    if row_10==0:
        bob.penup()
        bob.forward(100)
    elif row_10==1:
        bob.pendown()
        bob.forward(100)

    row_11=dum.randint(0,1)
    bob.teleport(0,-300)
    if row_11==0:
        bob.penup()
        bob.forward(100)
    elif row_11==1:
        bob.pendown()
        bob.forward(100)

    row_12=dum.randint(0,1)
    if row_12==0:
        bob.penup()
        bob.forward(100)
    elif row_12==1:
        bob.pendown()
        bob.forward(100)

    row_13=dum.randint(0,1)
    if row_13==0:
        bob.penup()
        bob.forward(100)
    elif row_13==1:
        bob.pendown()
        bob.forward(100)

    row_14=dum.randint(0,1)
    if row_14==0:
        bob.penup()
        bob.forward(100)
    elif row_14==1:
        bob.pendown()
        bob.forward(100)

    row_15=dum.randint(0,1)
    if row_15==0:
        bob.penup()
        bob.forward(100)
    elif row_15==1:
        bob.pendown()
        bob.forward(100)

    row_16=dum.randint(0,1)
    bob.teleport(0,-400)
    if row_16==0:
        bob.penup()
        bob.forward(100)
    elif row_16==1:
        bob.pendown()
        bob.forward(100)

    row_17=dum.randint(0,1)
    if row_17==0:
        bob.penup()
        bob.forward(100)
    elif row_17==1:
        bob.pendown()
        bob.forward(100)

    row_18=dum.randint(0,1)
    if row_18==0:
        bob.penup()
        bob.forward(100)
    elif row_18==1:
        bob.pendown()
        bob.forward(100)

    row_19=dum.randint(0,1)
    if row_19==0:
        bob.penup()
        bob.forward(100)
    elif row_19==1:
        bob.pendown()
        bob.forward(100)

    row_20=dum.randint(0,1)
    if row_20==0:
        bob.penup()
        bob.forward(100)
    elif row_20==1:
        bob.pendown()
        bob.forward(100)

    row_21=dum.randint(0,1)
    bob.teleport(0, -500)
    if row_21==0:
        bob.penup()
        bob.forward(100)
    elif row_21==1:
        bob.pendown()
        bob.forward(100)

    row_22=dum.randint(0,1)
    if row_22==0:
        bob.penup()
        bob.forward(100)
    elif row_22==1:
        bob.pendown()
        bob.forward(100)

    row_23=dum.randint(0,1)
    if row_23==0:
        bob.penup()
        bob.forward(100)
    elif row_23==1:
        bob.pendown()
        bob.forward(100)

    row_24=dum.randint(0,1)
    if row_24==0:
        bob.penup()
        bob.forward(100)
    elif row_24==1:
        bob.pendown()
        bob.forward(100)

    row_25=dum.randint(0,1)
    if row_25==0:
        bob.penup()
        bob.forward(100)
    elif row_25==1:
        bob.pendown()
        bob.forward(100)

    #Now make the collumns... one by one. *LOUDER SIGH*
    #Put it in the right spot
    bob.teleport(100, 0)
    #Make it face down
    bob.setheading(270)
    col_1=dum.randint(0,1)
    if col_1==0:
        bob.penup()
        bob.forward(100)
    elif col_1==1:
        bob.pendown()
        bob.forward(100)

    col_2=dum.randint(0,1)
    if col_2==0:
        bob.penup()
        bob.forward(100)
    elif col_2==1:
        bob.pendown()
        bob.forward(100)

    col_3=dum.randint(0,1)
    if col_3==0:
        bob.penup()
        bob.forward(100)
    elif col_3==1:
        bob.pendown()
        bob.forward(100)

    col_4=dum.randint(0,1)
    if col_4==0:
        bob.penup()
        bob.forward(100)
    elif col_4==1:
        bob.pendown()
        bob.forward(100)


    col_5=dum.randint(0,1)
    if col_5==0:
        bob.penup()
        bob.forward(100)
    elif col_5==1:
        bob.pendown()
        bob.forward(100)

    col_6=dum.randint(0,1)
    bob.teleport(200,0)
    if col_6==0:
        bob.penup()
        bob.forward(100)
    elif col_6==1:
        bob.pendown()
        bob.forward(100)

    col_7=dum.randint(0,1)
    if col_7==0:
        bob.penup()
        bob.forward(100)
    elif col_7==1:
        bob.pendown()
        bob.forward(100)

    col_8=dum.randint(0,1)
    if col_8==0:
        bob.penup()
        bob.forward(100)
    elif col_8==1:
        bob.pendown()
        bob.forward(100)

    col_9=dum.randint(0,1)
    if col_9==0:
        bob.penup()
        bob.forward(100)
    elif col_9==1:
        bob.pendown()
        bob.forward(100)


    col_10=dum.randint(0,1)
    if col_10==0:
        bob.penup()
        bob.forward(100)
    elif col_10==1:
        bob.pendown()
        bob.forward(100)

    col_11=dum.randint(0,1)
    bob.teleport(300,0)
    if col_11==0:
        bob.penup()
        bob.forward(100)
    elif col_11==1:
        bob.pendown()
        bob.forward(100)

    col_12=dum.randint(0,1)
    if col_12==0:
        bob.penup()
        bob.forward(100)
    elif col_12==1:
        bob.pendown()
        bob.forward(100)

    col_13=dum.randint(0,1)
    if col_13==0:
        bob.penup()
        bob.forward(100)
    elif col_13==1:
        bob.pendown()
        bob.forward(100)

    col_14=dum.randint(0,1)
    if col_14==0:
        bob.penup()
        bob.forward(100)
    elif col_14==1:
        bob.pendown()
        bob.forward(100)

    col_15=dum.randint(0,1)
    if col_15==0:
        bob.penup()
        bob.forward(100)
    elif col_15==1:
        bob.pendown()
        bob.forward(100)

    col_16=dum.randint(0,1)
    bob.teleport(400,0)
    if col_16==0:
        bob.penup()
        bob.forward(100)
    elif col_16==1:
        bob.pendown()
        bob.forward(100)

    col_17=dum.randint(0,1)
    if col_17==0:
        bob.penup()
        bob.forward(100)
    elif col_17==1:
        bob.pendown()
        bob.forward(100)

    col_18=dum.randint(0,1)
    if col_18==0:
        bob.penup()
        bob.forward(100)
    elif col_18==1:
        bob.pendown()
        bob.forward(100)

    col_19=dum.randint(0,1)
    if col_19==0:
        bob.penup()
        bob.forward(100)
    elif col_19==1:
        bob.pendown()
        bob.forward(100)

    col_20=dum.randint(0,1)
    if col_20==0:
        bob.penup()
        bob.forward(100)
    elif col_20==1:
        bob.pendown()
        bob.forward(100)

    col_21=dum.randint(0,1)
    bob.teleport(500,0)
    if col_21==0:
        bob.penup()
        bob.forward(100)
    elif col_21==1:
        bob.pendown()
        bob.forward(100)

    col_22=dum.randint(0,1)
    if col_22==0:
        bob.penup()
        bob.forward(100)
    elif col_22==1:
        bob.pendown()
        bob.forward(100)

    col_23=dum.randint(0,1)
    if col_23==0:
        bob.penup()
        bob.forward(100)
    elif col_23==1:
        bob.pendown()
        bob.forward(100)

    col_24=dum.randint(0,1)
    if col_24==0:
        bob.penup()
        bob.forward(100)
    elif col_24==1:
        bob.pendown()
        bob.forward(100)


    col_25=dum.randint(0,1)
    if col_25==0:
        bob.penup()
        bob.forward(100)
    elif col_25==1:
        bob.pendown()
        bob.forward(100)
    
    walls = row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9, row_10, row_11, row_12, row_13, row_14, row_15, row_16, row_17, row_18, row_19, row_20, row_21, row_22, row_23, row_24, row_25, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, col_10, col_11, col_12, col_13, col_14, col_15, col_16, col_17, col_18, col_19, col_20, col_21, col_22, col_23, col_24, col_25
    return walls

def solveability_check():
    solver=bob.Turtle()
    solver.color("#FF8800")
    solver.penup()
    solver.goto(50,0)
    solver.setheading(270)



def border_generation():
    bob.speed(0)
    bob.tracer()
    bob.penup()
    bob.goto(0,0)
    bob.forward(100)
    bob.pendown()
    bob.forward(500)
    bob.right(90)
    bob.forward(600)
    bob.right(90)
    bob.penup()
    bob.forward(100)
    bob.pendown()
    bob.forward(500)
    bob.right(90)
    bob.forward(600)

border_generation()
maze_generation()
solveability_check()


bob.hideturtle()
bob.done()