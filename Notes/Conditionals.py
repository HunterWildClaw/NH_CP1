# NH 2nd conditionals notes

#import libraries
import random
monster_hp = 30
dmg_modifier = 2
atk_bonus = 3
player_hp = 25

roll = random.randint(1,20)


#DnD attack generater for a dice roll thingy.

if roll == 20:
    print(f"You You rolled a crit! Double your damage.")
    attack = random.randint(1,8) + random.randint(1,8) + dmg_modifier
    monster_hp -= attack
    print(f"You did {attack} damage to the monster!")
elif roll+atk_bonus > 10:
    print(f"You hit!")
    attack = random.randint(1,8) + dmg_modifier
    monster_hp -= attack
    print(f"You did {attack} damage to the monster!")
elif roll <= 10:
    if roll == 1:
        print(f"You rolled a critical failure! The monster gets a free attack!")
        damage = random.randint(1,10) +2
        player_hp -= damage
        print(f"You took {damage} you now have {player_hp} HP.")
    else:
        print("You missed!")
else:
    print("Uhh that shouldn't be possible...")

print("Your turn is over.")

if monster_hp and monster_hp > 0:
    print("It is the monsters turn.")
else:
    print("The monster is dead.")


#num = int(input("Enter a random number: "))

#if num > 0:
    #print(f"Your number was {num}. That number is a positive number.")
#elif num < 0:
    #print(f"Your number was {num}. That's a negative number.")
#elif num == 67:
    #print(f"{num}! I love six seven!")
#else:
    #print(f"Your number is 0. Oof")


