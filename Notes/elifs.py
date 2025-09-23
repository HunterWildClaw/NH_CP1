#NH 2nd Elifs and Logical Operators Notes:

homework = True
chores = True
room = True

if homework and chores and room:
    print("You can go to your friends house.")
elif not chores or not room:
    print("Do your chores!!!")
else:
    print("Go do your homework!!!")

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "HunterWildClaw":
    if password == "Albi0n 0nline":
        print("Welcome Hunter!")
    else:
        print('Incorrect password. Try again.')
if username == "HunterWildClaw" and password == "Albi0n 0nline":
    print("Welcome Hunter!")
elif username == "Howlixier" and password == "Albi0n0nline":
    print("Welcome Howlixier!")
elif username == "Landon" and password == "Allied":
    print("Welcome, Landon.")
else:
    print("That is not valid.")