# NH 2nd Combat Program
import time as sleep

player_def = 0
player_atk = 0
player_hp = 0
player_name = input("Welcome to the Training Dojo! Let's get to know you. \nWhat's your name? ")
player_class = input(f"Hello, {player_name}! It's good to meet you. What class are you?\nPress '1' to be a Warrior! \nPress '2' to be a Mage! \nPress '3' to be a Rogue! \nOr press '4' to be a Hunter!")
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