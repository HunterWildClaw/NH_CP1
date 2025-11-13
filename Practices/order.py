# NH 2nd Order Up!
food_cart=[]
cost=0
# Make the dictionary
food_menu = {
    "Main Meals": {
        "Burger": 4.99,
        "Hot Dog": 3.59,
        "Chicken Noodle Soup": 5.39,
        "Corn Dog": 3.79
    },
    "Side Dishes": {
        "French Fries": 2.59,
        "French Toast Strips": 2.79,
        "Salad": 2.69,
        "Bowl o' Goldfish": 1.99
    },
    "Soda": {
        "Root Beer": 3.99,
        "Sprite": 3.99,
        "Red Cream Soda": 4.00,
        "Dr. Pepper": 3.99
    }
}
#Make a function for the customer's order
def order(cost, food_cart):
    #Intrudoce customer and give them their menu
    print(f"Hello customer! Welcome to Chubby's! Here's your menu.\n{food_menu}")
    #Then ask for what they want
    food_cart.append(input('What main course do you want?'))
    food_cart.append(input('What 2 side dishes do you want?'))
    food_cart.append(input('What soda do you want?'))
    for food in food_cart:
        



#Use function
order(cost, food_cart)