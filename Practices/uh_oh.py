#NH 2nd factorial pseduocode

#define function called factor
def factor():
    #while it so that it loops
    while True:
        #input asking for a number
        number=int(input("Give a random number off the top of your head: "))
        #check if the input is an integer
        if number is int:
            #once integer is inputed show the number
            print(number)
        #And use a for statement to get every number <0 before number and multiply them all.
            for i in number:
                i=number-1
                if i==0:
                    break
                else:
                    number*i   
        #loops over if not
        elif number is not int:
            continue

factor()
