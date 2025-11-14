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
def order(menu):
    #Intrudoce customer and give them their menu
    print(f"Hello customer! Welcome to Chubby's! Here's your menu.\n{menu}")
    #Then ask for what they want and put it in the list
    food_cart=['','','','']
    while food_cart[0] not in menu['Main Meals'].keys:
        food_cart[0]=input('What main course do you want?')
    while food_cart[1] not in menu['Side Dishes'].keys:        
        food_cart[1]=input('What would you like for your first side dish?')
    while food_cart[2] not in menu['Side Dishes'].keys:
        food_cart[2]=input('What would you like for your second side dish?')
    while food_cart[3] not in menu['Soda'].keys:
        food_cart[3]=input('What soda do you want?')
    return food_cart


#name the function something else for future use
items=order(food_menu)