# NH 2nd Lists Notes.
import random

names = ["Bob", "Hunter", "Jeff", 5, 3.14159, True]

print(names)
print(names[2])
print(names[random.randint(1,len(names))])
print(random.choice(names))
names[-1] = False
names.extend(["Treyson", "Joshy"])
names += ["Joseph", "Israel", "Zee"]
names.remove(3.14159)
x = names.index(5)
names.insert(3, "Nathan")
names.pop(x)
print(names)

board = [[1,2,3],
        [4,5,6],
        [7,8,9]]

board[1][1] = "X"

print(board)
# List (changeable, ordered)
# Tuple (Not changeable, ordered)
classes = ("Bard", "Monk", "Barbarian", "Paladin")

# Set (changeable, unordered)
fruit = {"Apple", "Orange", "Strawberry", "Kiwi"}
print(fruit)