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




bob.done()