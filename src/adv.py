from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# items
items = {'Axe Body Spray': Item("Axe Body Spray,", "Bro you smell..."),
         'Yu-Gi-Yo Cards': Item("Yu-Gi-Yo Cards,", "Incase you come across a challenger..."),
         'Torch': Item("Torch,", "Show Me The Light!")
         }

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#Link Items

room['outside'].items.append(items['Torch'])
room['overlook'].items.append(items['Yu-Gi-Yo Cards'])
room['narrow'].items.append(items['Axe Body Spray'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input('\nWelcome Traveler! What is your name...? \n')
player = Player(name, room['outside'])

print(f'\nWelcome {player.name} to Juggalo land... \n')
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
user_is_playing = True

while user_is_playing:
    print(f'\nYou are at the {player.current_room.name}\n')

    print(f'\n {player.current_room.description} {player.current_room.list_items()}')

    user_input = input(
        " Enter (n,e,s,w) to continue \n Want To Quit The Game? (q) \n What will you do? ")

    if user_input in ["n", "e", "s", "w"]:
        print("Heads towards...")
        player.move(user_input)
    elif user_input == "q":
        print("Until Next Time Traveler")
        user_is_playing = False
    else:
        print("The Movement You Have Entered Is Not Allowed")