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


# conditional evaluate
# Respond based on the player's decision


while (True):
    decision = input("\t1. Take the left path i to the dark woods\n "
                     "\t2. Take the right path towards the mountain pass\n"
                     "\t3. Go into a nearby Cave\n"
                     "\t4. Explore the Hidden Valley\n"
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
        if player1.has_lantern == True:
            print("You go into the dark cave")
            add_to_inventory("Treasure", player1)
        else:
            print("It's too dark in the cave. Try to find something to illuminate your way")
    elif decision == "4":
        if player1.has_map:
            print("You go into the hidden valley")
            add_to_inventory("Rare Herbs", player1)
        else:
            print("You can't find the valley without directions")
    elif decision == "5":
        print("Confused, you stand still, unsure of what to do.")
    elif decision == "i":
        print (player1.inventory)
    else:
        print("That is not a valid choice")
