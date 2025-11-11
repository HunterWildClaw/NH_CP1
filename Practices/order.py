# NH 2nd Order Up!

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
def order(choices, food):
    food_cart=[]
    price=0
    #Give them their options
    for yummy in choices:
        print(yummy)
        #Ask what they want
        what_they_want=input("Hello customer! Welcome to Chubby's!\nHere's your menu. Please take your time. {}")
        while True:
            for yummy in what_they_want:
                item=input("What you like to order, my good sir?").strip().title()
                if item in choices:
                    food_cart.append[item]
                    price += choices[item]