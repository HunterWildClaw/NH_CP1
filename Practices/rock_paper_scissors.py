# NH 2nd Rock Paper Scissors
import random
import time

score = 0
while True:
    choice = input("Hello! Would you like to play Rock, Paper, Scissors? Or would you like to quit. Push 'p' to play and 'q' to quit. Or push 's' to see your score?: ").lower().strip()
    if choice == 'p':
        print("Alright. You have chosen death!")
        player_move = input("Ok so you need to choose rock, paper, or scissors. Which one? ").lower().strip()
        print("Rock!")
        time.sleep(0.5)
        print("Paper!")
        time.sleep(0.5)
        print("Scissors!")
        cpu_move = random.randint(1,3)

        if cpu_move == 1 and player_move == "rock":
            print("We both did rock! Tie! You earn no points.")

        elif cpu_move == 1 and player_move == "paper":
            print("I did rock and you did paper! You win! You earn a point!")
            score += 1
        elif cpu_move == 1 and player_move == "scissors":
            print("I did rock and you did scissors! I win! You earn no points.")

        elif cpu_move == 2 and player_move == "rock":
            print("I did paper and you did rock! I win! No points for you! HAHAHAHA!!!")

        elif cpu_move == 2 and player_move == "paper":
            print("I did paper and you did paper! Tie! No points earned.")

        elif cpu_move == 2 and player_move == "scissors":
            print("I did paper and you did scissors! You get a point!")
            score += 1
        elif cpu_move == 3 and player_move == "rock":
            print("I did scissors and you did rock! You win! Here's a point.")
            score += 1
        elif cpu_move == 3 and player_move == "paper":
            print("I did scissors and you did paper! I win! MWUHAHAHA!")

        elif cpu_move == 3 and player_move == "scissors":
            print("I did scissors and you did scissors! Tie!")

        else:
            print("I need rock, paper, or scissors. Not that. Try again.")
    elif choice == 's':
        print(score)
    elif choice == 'q':
        print("Aw ok. Cya!")
        break
    else:
        print("I need either a 'p' 'q' or 's'.")