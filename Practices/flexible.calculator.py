#NH 2nd Flexible Calculator

#import math cuz its awesome
import math

#Make a function for the whole thing
def calculation(*numbers):
    #get the numbers
    numbers=input("Type what numbers you want, seperated by spaces: ")
    #turn it to a list
    list=numbers.split()
    #show them they're nums
    print(list) 
    calculation_operation = input("What operation would you like me to perform with you're numbers? We can do sum, product, max or mim: ")
    #If they chose to add the numbers...
    if calculation_operation == "sum":
        #Add 'em up
        total = sum(list)
        #give em the total
        print(f"The sum of you're numbers is {total}!")
        #If they chose product...
    elif calculation_operation == "product":
        product=math.prod(list)
        print(f"The product of those numbers is {product}")

#Call the function
calculation()