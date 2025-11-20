#NH 2nd Squared Numbers 
#Make a list of nums
numbers=[3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285] # Now make a thing to square all those numbers. Then use the lambda thing to perform the calculation
squares=list(map(lambda num: num*num, numbers)) # Now print out all of the outcomes
for i, num in enumerate(numbers): print(f"{num} squared is {squares[i]}")