'''
Adventure Game
Author: Bobby Swanson
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.

'''

from Player import Player


def add_to_inventory(item, player):
    player.inventory.append(item)
    print("You picked up", item)



def describe_area():
# Describe the starting area
    starting_area = """
    You find yourself in a dark forest.
    The sound of rustling leaves fills the air.
    A faint path lies ahead, leading deeper into the unknown...
    """
    print(starting_area)

def welcome_player():
    print("Welcome to the Adventure Game!")
    print("You're journey begins here...")

    # Ask for the player's name
    player_name = input("What is your name, adventurer? ")

    # Use an f-string to display the same message in a more readable way
    print(f"Welcome, {player_name}! Your journey begins now.")
    player1 = Player(player_name)
    return player1


player1 = welcome_player()

describe_area()


# Ask the player for their first decision
decision = input("Do you wish to take the path? (yes or no): ").lower()

# conditional evaluate
# Respond based on the player's decision
if decision == 'yes':
    print("Brave choice, {player_name}! You step onto the path and venture forward.")
elif decision == "no":
    print(player_name + ", you decide to wait. Perhaps courage will find you later.") # Concatenation example
else:
    print("Confused, you stand still, unsure of what to do.")

while (True):
    decision = input("\t1. Take the left path i to the dark woods\n "
                     "\t2. Take the right path towards the mountain pass\n"
                     "\t3 Go into a nearby Cave\n"
                     "\t4 Explore the Hidden Valley\n"
                     "\t5. Stay where you are \n"
                     "\tType 'i' to view your inventory").lower()


    if decision == "1":
        print(f"You go into the dark woods")
        add_to_inventory("lantern", player1)
        player1.has_lantern = True
    elif decision == "2":
        print("You go towards tyhe mountain pass")
        add_to_inventory("map", player1)
        player1.has_map = True
    elif decision == "3":
        print("You go into the dark cave")
    elif decision == "4":
        print("You go into the hidden valley")
    elif decision == "5":
        print("Confused, you stand still, unsure of what to do.")
    elif decision == "i":
        print (player1.inventory)
    else:
        print("That is not a valid choice")