# 2nd NH Crew Share

total_money = int(input("Hey so name a random number. (And this works better if it's a big number.) Enter number: "))
crew_members = int(input("And now we need a small number. Enter number: "))
print("So here's the story.\n The crew earned a whole bunch of money on the last outing, but the captain didn't have time to divvy it all up before release everyone to port. He gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares \n The captain of the crew gets 7 shares (equal portions of the treasure) \n The first mate gets 3 shares. \n Each crew member of the crew then gets 1 share.")
print(f"The crew earned the big number you put before. This one: {total_money}. The small number is the number of crew members. This one: {crew_members}. Now we split it up. *cracks knuckles and pops neck* Watch me cook")
one_share = total_money / (10 + crew_members)
print(f"The captain gets {one_share * 7:.2f}$\n The first mate guy gets a whopping {one_share * 3:.2f}$\n Each indivual crew member also needs to recieve {one_share-500:.2f}$ even after accepting their 500$ dollars.")
