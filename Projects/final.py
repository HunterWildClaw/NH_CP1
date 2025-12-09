#NH 2nd Final Project
import time

#PLAYER_NAME=input(“Welcome player. What is your name?”)
player_name=input("Hello, Player! What name would you like to play as?\nEnter here: ")
#PLAYER_HP=12
player_hp=12
#MASTER SWORD = 12
master_sword=12
#STICK=3
stick=4
#MELEE WEAPON = “stick”
melee_weapon = stick or master_sword
#PLAYER_ATK=3+MELEE_WEAPON
player_atk=3+melee_weapon
#Ranged stuff
travelers_bow=8
royal_guards_bow = 16
bow=travelers_bow or royal_guards_bow
ranged_weapon=travelers_bow
ranged_atk=0+ranged_weapon

#Show the player what the world’s like right now and give the history. Also explain that they’re the hero and they are stuck on a sky island.
print(f"Hello and welcome {player_name}! This is the world of Hyrule. A place of fantasy and beauty. And a place of death. The Demon King has rose up and summoned his demon army. The world is in chaos and turmoil. But a hero rose up. Found the Master Sword. And struck against the Demon King, critically wounding him. But the Demon King has one last trick. He corrupted the Hero.\nThe Hero failed.\nBut Now you're here!")
time.sleep(7)
print("You can save the world. You can slay the Demon King!\n\nBut first, get off this rock in the sky. 😄 That's right. You're stuck on a sky island. It's a moderately large one. Probably like the size of the BYU campus...")
time.sleep(6)
print("Anyhoo, there is a powerful zonai guardian. It's like a guardian from Breath of the Wild but it's all zonai looking. It's emerald colored and shoots a teal laser.\nKill him to find a sleeping aerocuda.")
time.sleep(5)
#And also give them a starting stick and a Traveler’s Bow for starting weapons.
print("You have a TRAVELER'S BOW for your ranged weapon. It gives plus 8 ranged damage.")
time.sleep(4)
print(f"You also start with a stick. It gives plus 4 to your attack. You already have 3 attack as well.")
time.sleep(3)
print('You start with 12 health. That is pretty much 3 hearts.')
#Make a function for combat with four arguments of monster hp, monster atk, player atk and player hp and call it combat
#While loop it
#		Give player option for bow atk if far away or melee atk if close up
#		Give monster chance to block atk if they have shield
#		If monster fails to block, subtract monster health from player atk dmg
#		If monster lives, they get to go now
#		Monster atks with either melee weapon or bow depending on what they have
#		If bow the player can only dodge
#		If melee give player option to block monster atk
#		If player fails to block, subtract player hp from monster atk
#		If player hp < 0, bring code back to the start of the room
#Def tabantha()
#	An ice chuchu with 15 hp and 2 frost atk attacks player
#	Use combat function and insert 15 and 2 for mobs stats and player stats for stats
#	If player dies reset
#	Else if monster dies player has option to eat to heal if low health or move on
#		If they move on
#			They have to fight an Abominable Snowman
#			It has 30 hp and 15 atk
#			If they die, restart them to the chuchu fight
#			Elif they win
# 				teleport them to lookout landing
#               Add 4 more maximum health
#				Hyrule Castle is shaking slightly
                print("You see Hyrule Castle shaking slightly in the distance.")
#				Ask if they want to stay and shop
#				If yes, activate market function
#				If no, ask where they want to go.
# (Same regions as before minus the region they just did)
#		Elif they eat
#			Display their inventory and show their food
#			If they have food
#				Give them option to eat it
#				If they eat it
#					Take it from inventory
#					Give player 4 hp
#					Then do same stuff as if they continued
#Def gerudo()
#	Electric chuchu attacks player
#		Same stats as ice chuchu but lightning instead of ice.
#		Combat function with 15 monster hp and 2 electric atk
#		If player dies reset to beginning of fight
#		So basically same as tabantha()
#		But the boss is a giant sand worm with 30 hp and
#Have player start with 12 hp and 4 hp = 1 heart
#To get down from sky island, player must kill a zonai guardian and find a sleeping aurocouda and hop on and fly down. Upon landing in Hyrule Field, you must find and kill The Hinox who guards the Master Sword
#
#After killing him using the combat function, (Hinox has 20 hp and 3 atk) then have player loot master sword, increasing his melee atk power by 10, or increase it by 20 against gloom creatures. Player then goes to Lookout Landing and talks to people. Give player option of who to talk to. Also have player find a royal guards bow. Then give player option to go to either Tabantha, Eldin, Lanaryu, tabantha sky, gerudo. After completing all of those regions, they can then go to Hyrule castle
# So throughout the game player loots items like monster horns that increase player atk against that type of monster. So if player consumes boko horn, player atk against boko is increase. Does not stack.
#The way inventory works is that we will have a dictionary and keys for mob horns, weapons, and food. Anytime player loots monster horn, add it into the key monster horns as a value. Etc with the others.
#So ask player if they wanna buy or sell from merchants (make a variable called Rupees for currency.)The player starts with 20 rupees.
#Make a function called market with one argument called player currency.
#	While Loop it!
    #	Give player option to either sell or buy or leave
    #	If player chooses to sell
    #		Show player inv
    #		Ask player to select one item
    #		Then sell item and give player 20 rupees and add them to player currency
    #	Elif player chooses to buy
    #		Show player merchant wares
    #		If merchant is weapons merchant
    #			Display weapons
    #		Elif merchant is food merchant
    #			Display food
    #		Give player option to choose an item or leave
    #		If player chooses to leave
    #			Close merchant
    #		Elif player chooses to select item
    #			Take 20 rupees from player and put item in player inventory
    #		Ask player if they would like to stay and spend more money or leave
    #		If they would like to shop more
    #			Loop it
    #		Elif they wanna leave
    #			Close shop
    #	Elif player chooses to leave
    #		Close shop
#Call function every time they go to merchant
#Now have them leave lookout landing
#Ask if they want to go to tabantha, eldin, tabantha sky, gerudo, lanaryu, or eldin caves
#If tabantha
#	tabantha()
#If gerudo
#	gerudo()
#If eldin
#	eldin()
#If lanaryu
#	lanaryu()
#If eldin caves
#	eldin_caves()
#If tabantha sky
#	Tabantha_sky()
#Once they beat all regions
#They go to hyrule castle and fight boss
#Boss is the demon king
#Secret room in hyrule castle before boss
#Demon King has 50 hp and 10 atk
#If he dies, end game
#If player dies, restart fight
