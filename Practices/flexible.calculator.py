#NH 2nd Flexible Calculator

#Make a function for:
def calculation(*numbers):
    #Asking person if they want the sum, average, maximum, minimum, or product
        calculation_operation=input("We can get you the sum, average, min, max, or product! Which one would you like for these numbers? Please choose one: ")
        list = calculation_operation.split()
        print(list)
    # If they chose sum:
        if calculation_operation == "sum":
            sum = ""
            for number in numbers:
                  sum += number
            print(sum)
        #add up all the numbers
        #Then show the total

    # If they chose average
        #add all the numbers up then divide by the amount of numbers
        #Then show the average

    #If they chose maximum or minumum 
        # just find the smallest or largest number and print it

    #If they chose product
        #Multiply the numbers and give the "product"


#Make the whole thing a while loop so they can do it over and over again.
while True:
    #Ask for numbers
    numbers = []
    numbers.append(input("What numbers would you like to give at our humble calculation factory? Just whole numbers for now: "))
    if numbers == int or float:
        print('gj')
    #Ask person if they want the sum, average, maximum, minimum, or product

    # If they chose sum:
        #add up all the numbers
        #Then show the total

    # If they chose average
        #add all the numbers up then divide by the amount of numbers
        #Then show the average

    #If they chose maximum or minumum 
        # just find the smallest or largest number and print it

    #If they chose product
        #Multiply the numbers and give the "product"