#NH 2nd Shopping List Manager

shopping_list = []

while True:
    action = input(" Select '1' to add an item. \n Select '2' to remove an item. \n Select '3' to view your list. \n Select '4' to leave. \n").strip()
    if action == "1":
        new_item = input("Enter item: ")
        if new_item not in shopping_list:
            shopping_list.append(new_item)
            print("Item added.")
        else:
            print("This item is already in list.")
    elif action == "2":
        removed_item = input("What would you like to remove?")
        if removed_item in shopping_list:
            shopping_list.remove(removed_item)
            print("Item removed.")
        else:
            print("Item not found in shopping list.")
    elif action == "3":
        print(shopping_list)

    elif action == "4":
        print("Goodbye!")
        break

    else:
        print("You need to input a number from 1-4.")