#NH 2nd Functions notes
# all imports
# Set global variables
num = 0
player_hp = 100
monster_hp = 100

# Write your functions
def add(x, y):
    return x+y

def initials(name):
    names = name.split(" ")
    initial = ""
    for name in names:
        initial += name[0]
    return initial

def attack(dmg, turn):
    if turn == "player":
        return monster_hp - dmg, player_hp
    else:
        return monster_hp, player_hp - dmg


# Write the rest of the code
while num < add(5,5):
    print("Duck")
    num += 1
print("Goose")
print(f"Result is : {add(-6519146, 36516)}")
total = add(689461, 654894)
print(add(add(3.14,.85), 10))
add(42, 7)



print(f"Tia's initials are: {initials("Tia LaRose")}")
print(f"Xavier's initials are: {initials("Xavier LaRose")}")
moster_hp, player_hp = attack(15, "monster")
print(f"Player Health: {player_hp}")
print(f"Monster Health: {monster_hp}")

player_hp, monster_hp = attack(15, "player")
print(f"Player Health: {player_hp}")
print(f"Monster Health: {monster_hp}")

print(f"a = {ord("a")}")
print(f"100 = {chr(100)}")