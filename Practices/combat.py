# NH 2nd Combat Program
import time as sleep
import random
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
        warrior_hp = player_hp
        player_atk += 5
        warrior_atk=player_atk
        player_def += 100
        warrior_def=player_def
        print(f"Your stats are {warrior_hp} hp, {warrior_atk} attack, and {warrior_def} defense.")
        break
    elif player_class == '2':
        print("Alright! You are a Mage! Generating your stats now...")
        sleep.sleep(1)
        player_hp += 30
        mage_hp = player_hp
        player_atk += 50
        mage_atk=player_atk
        player_def += 5
        mage_def=player_def
        print(f"Your stats are {mage_hp} hp, {mage_atk} attack, and {mage_def} defense.")
        break
    elif player_class == '3':
        print("Alright! You are a Rogue! Generating your stats now...")
        sleep.sleep(1)
        player_hp += 40
        rogue_hp = player_hp
        player_atk += 40
        rogue_atk=player_atk
        player_def += 30
        rogue_def=player_def
        print(f"Your stats are {rogue_hp} hp, {rogue_atk} attack, and {rogue_def} defense.")
        break
    elif player_class == '4':
        print("Alright! You are a Hunter! Generating your stats now...")
        sleep.sleep(1)
        player_hp += 35
        hunter_hp = player_hp
        player_atk += 40
        hunter_atk=player_atk
        player_def += 30
        hunter_def=player_def
        print(f"Your stats are {hunter_hp} hp, {hunter_atk} attack, and {hunter_def} defense.")
        break
    else:
        print("Please press 1, 2, 3, or 4. Do not troll.")
        break
sleep.sleep(1)
monster=''
player=''
turn_determination = random.randint(1,2)
if turn_determination == 1:
    turn_determination=monster
elif turn_determination==2:
    turn_determination==player


if turn_determination == monster:
    monster_move = input("Ok, so. You were wandering in the dark woods when a fierce spiderling leaps at you from above.")
elif turn_determination == player:
    player_move = input("Ok, so. You were wandering in the dark woods when a fierce spiderling leaps at you from above. You dodge and roll to the side. Your health potions clink against your defense potions. You also remember your rage potions to increase your next hit. Would you like to drink one of the potions? Or just fight? Press '1' to drink and '2' to fight: ")

if player_move == '1':
    player_potion_choice = input("Would you like to drink a potion to increase your health, defense, or attack? press '1' for health, '2' for defense, or '3' for attack: ")
    if player_potion_choice == '1':
        player_hp += health_potion
        print(f"You now have {player_hp} health!")
    elif player_potion_choice == '2':
        player_def += defense_potion
        print(f"You now have {player_def} defense points!")