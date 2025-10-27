# NH 2nd Combat Program
import time as sleep
import random

monster_hp = 50
monster_atk = 10
monster_def = 20
rage_potion = 15
defense_potion = 15
health_potion = 15
player_def = 0
player_atk = 0
player_hp = 0
player_name = input("Welcome to the Training Dojo! Let's get to know you. \nWhat's your name? ")
player_class = input(f"Hello, {player_name}! It's good to meet you. What class are you?\nPress '1' to be a Warrior! \nPress '2' to be a Mage! \nPress '3' to be a Rogue! \nOr press '4' to be a Hunter!\nEnter class: ")
while player_class:
    if player_class == '1':
        print("Alright! You are a Warrior! Generating your stats now...")
        sleep.sleep(1)
        player_hp += 50
        player_atk += 5
        player_def += 100
        print(f"Your stats are {player_hp} hp, {player_atk} attack, and {player_def} defense.")
        break
    elif player_class == '2':
        print("Alright! You are a Mage! Generating your stats now...")
        sleep.sleep(1)
        player_hp += 30
        player_atk += 50
        player_def += 5
        print(f"Your stats are {player_hp} hp, {player_atk} attack, and {player_def} defense.")
        break
    elif player_class == '3':
        print("Alright! You are a Rogue! Generating your stats now...")
        sleep.sleep(1)
        player_hp += 40
        player_atk += 40
        player_def += 30
        print(f"Your stats are {player_hp} hp, {player_atk} attack, and {player_def} defense.")
        break
    elif player_class == '4':
        print("Alright! You are a Hunter! Generating your stats now...")
        sleep.sleep(1)
        player_hp += 35
        player_atk += 40
        player_def += 30
        print(f"Your stats are {player_hp} hp, {player_atk} attack, and {player_def} defense.")
        break
    else:
        print("Please press 1, 2, 3, or 4. Do not troll.")
        break


sleep.sleep(1)
monster='Monster'
player='Player'
turn_determination = random.randint(1,2)
print(turn_determination)
if turn_determination == 1:
    turn_determination=monster
elif turn_determination==2:
    turn_determination==player
else:
    print("Error!!!")

if turn_determination == monster or 1:
    if monster_atk > player_def:
        player_hp -= monster_atk
        print(f"Ok, so. You were wandering in the dark woods when a fierce spiderling leaps at you from above and scratches your head. It deals {monster_atk} damage! You now have {player_hp} health!")
    elif monster_atk < player_def:
        player_move = input("Ok, so. You were wandering in the dark woods when a fierce spiderling leaps at you from above. You dodge and roll to the side. Your health potions clink against your defense potions. You also remember your rage potions to increase the power of your next hit. Would you like to drink one of the potions? Or just fight? Press '1' to drink and '2' to fight: ")
        if player_move == '1':
            player_potion_choice = input("Would you like to drink a potion to increase your health, defense, or attack? press '1' for health, '2' for defense, or '3' for attack: ")
            if player_potion_choice == '1':
                player_hp += health_potion
                print(f"You now have {player_hp} health!")
            elif player_potion_choice == '2':
                player_def += defense_potion
                print(f"You now have {player_def} defense points!")
            elif player_potion_choice == '3':
                player_atk += rage_potion
                print(f"You now have {player_atk} attack power!")
            else:
                print("Please do '1', '2', or '3'. Do not troll.")
        elif player_move == '2':
            if player_atk > monster_def:
                monster_hp -= player_atk
                print(f"You hit! The monster now has {monster_hp} health!")
            elif player_atk < monster_def:
                print("You missed! L bozo")
elif turn_determination == player or 2:
    player_move = input("Ok, so. You were wandering in the dark woods when a fierce spiderling leaps at you from above. You dodge and roll to the side. Your health potions clink against your defense potions. You also remember your rage potions to increase the power of your next hit. Would you like to drink one of the potions? Or just fight? Press '1' to drink and '2' to fight: ")
    if player_move == '1':
        player_potion_choice = input("Would you like to drink a potion to increase your health, defense, or attack? press '1' for health, '2' for defense, or '3' for attack: ")
        if player_potion_choice == '1':
            player_hp += health_potion
            print(f"You now have {player_hp} health!")
        elif player_potion_choice == '2':
            player_def += defense_potion
            print(f"You now have {player_def} defense points!")
        elif player_potion_choice == '3':
            player_atk += rage_potion
            print(f"You now have {player_atk} attack power!")
        else:
            print("Please do '1', '2', or '3'. Do not troll.")
    elif player_move == '2':
        if player_atk > monster_def:
            monster_hp -= player_atk
            print(f"You hit! The monster now has {monster_hp} health!")
        elif player_atk < monster_def:
            print("You missed! L bozo")
else:
    print('Error! Something went wrong!')