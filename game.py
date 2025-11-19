'''
Adventure Game
Author: Bobby Swanson
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.

'''

from Player import Player





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


def add_to_inventory(item, player):
    if not item in player.inventory:
        player.inventory.append(item)
        print("You picked up", item)


def explore_dark_woods(player):
    print(f"You go into the dark woods")
    add_to_inventory("lantern", player1)
    player1.has_lantern = True

def explore_mountain_pass(player):
    print("You go towards the mountain pass")
    add_to_inventory("map", player1)
    player1.has_map = True

def explore_cave(player):
    if player1.has_lantern == True:
        print("You go into the dark cave")
        add_to_inventory("treasure", player1)
    else:
        print("It's too dark in the cave. Try to find something to illuminate your way")
        player.health -= 10

def explore_hidden_valley(player):
    if player1.has_map:
            print("You go into the hidden valley")
            add_to_inventory("rare herbs", player1)
    else:
        print("You can't find the valley without directions")
        player.health -= 10

def stay_still(player):
    print("Confused, you stand still, unsure of what to do.")
    player.health -= 10

def check_win(player):
    if "treasure" in player.inventory and "rare herbs" in player.inventory:
        print("You have won the game!")
        return True
    else:
        return False
    
def check_lost(player):
    if player.health <= 0:
        print("Your health has gone to 0. You died!")
        return True
    else:
        return False

player1 = welcome_player()


describe_area()

has_won = False

# Ask the player for their first decision


# conditional evaluate
# Respond based on the player's decision


while (not has_won):
    decision = input("\t1. Take the left path into the dark woods\n "
                     "\t2. Take the right path towards the mountain pass\n"
                     "\t3. Go into a nearby Cave\n"
                     "\t4. Explore the Hidden Valley\n"
                     "\t5. Stay where you are \n"
                     "\tType 'i' to view your inventory").lower()


    if decision == "1":
        explore_dark_woods(player1)
               
    elif decision == "2":
        explore_mountain_pass(player1)
    
    elif decision == "3":
       explore_cave(player1)

    elif decision == "4":
        explore_hidden_valley(player1)

    elif decision == "5":
        stay_still(player1)

    elif decision == "i":
        print (player1.inventory)
    else:
        print("That is not a valid choice")

    print("Your health is:", player1.health)
    has_lost = check_lost(player1)
    if has_lost:
        break
    has_won = check_win(player1)




