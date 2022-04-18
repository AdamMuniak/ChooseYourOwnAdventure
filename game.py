#!/usr/bin/python3
from time import sleep
import os
import sys
import textwrap

### How to use textwrap with type print?

rooms = {
	'Room_1': {
		'Message': 'You wake on a cold hard floor. As your eyes adjust to the darkness you recognize your surroundings as what must be a cell in the castle dungeon.',
		'Options': {'1': {'Message':'Call for help?','Result':'Room_2'}, 
					'2': {'Message': 'Search the room?', 'Result':'Room_5'}}
	},
	'Room_2': {
		'Message': 'You rouse yourself and call out for help. After a few moments you see the flicker of fire as someone approaches. You hear the clink of keys and the squeaky turn of a lock as the door swings open. The figure steps into the cell and reaches for your arm.',
		'Options': {'1': {'Message':'Go with the man?','Result':'Room_4'}, 
					'2': {'Message': 'Fight?', 'Result':'Room_3'}}
	},
	'Room_3': {
		'Message': 'You slap the hand of the figure away and charge forwards pushing them to the side as you rush through the door. The hallway outside is just as dark as the cell. Looking left you see light at the far end of the cooridor. As you turn to run an explosion of pain rips through your body and a sword tip emerges from your stomach. As the blood begins to flow from the wound the world flickers and darkens as you sink to the floor.',
		'Options': {'1': {'Message':'You Died.','Result':'END'}}
	},
	'Room_4': {
		'Message': 'The figure leads you out into a hallway and down the cooridor towards a light at the far end. A door opens and you\'re free to go.',
		'Options': {'1': {'Message':'You Win','Result':'END'}}
	},
	'Room_5': {
		'Message': 'You feel blindly around the dark cell and your hand gribs steel. A knife is added to inventory.',
		'Options': {'1': {'Message':'Call for help?','Result':'Room_2'}},
		'Items' : {'1': {'Name': 'Knife'}}
	}
}

inventory = dict()

#### Functions ####

# Clear Screen
def clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   # print out some text

# Print text like it's being typed
def type_print(message):
    for char in message:
        # print(char, end='')
        # sleep(.05)
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.05)

    print('\n')
    #sleep(.1)

# Welcome Message
def welcome():
	clear()
	type_print('\nWelcome to the Game!')
	sleep(1)
	clear()

# Check for Game Over
def game_over(current_room):
	# Check for END Game
    if current_room == 'END':
    	clear()
    	print('GAME OVER.')
    	sleep(2)
    	clear()
    	exit()

# Build Menu
def build_menu(current_room):
    
    # Build Menu based on current room
    index = 1
    menu_options = dict()

    for k,v in rooms[current_room]['Options'].items():
    	# Add rooms options
        menu_options[index] = v['Message']

        # Increment index
        index += 1

    # Add Exit
    menu_options[index] = 'Exit'

    # return menu
    return(menu_options)

# Print Menu
def print_menu(current_room, menu_options):
	# Set textwrap for 80 columns
	print(textwrap.fill((rooms[current_room]['Message']), 80))
	print('\n')
	for index, value in menu_options.items():
		print(str(index)+')',value)

# User Choice
def make_choice(current_room, menu_options):
    while True:
        print_menu(current_room,menu_options)
        choice = input("\nMake Your Choice:")
        if (choice.isnumeric()) and (int(choice) in menu_options.keys()):
            clear()
            # Update Room
            return(choice)
        else:
            clear()
            print('\n...path unknown...')
            sleep(1)
            clear()
            #print_menu(current_room, menu_options)
    print('\n')

# Update Current Room
def update_room(choice, current_room, menu_options):
	for k,v in menu_options.items():
		if choice == k:
			if v == 'Exit':
				clear()
				print('\n Bye Bye, stay safe...')
				sleep(2)
				clear()
				exit()
			else:
				search = v
				for index,option in rooms[current_room]['Options'].items():
				 	for k,v in option.items():
				 		if v == search:
				 			return(rooms[current_room]['Options'][index]['Result'])

# Pickup item
# Need to work out game logic to add item per room labels
def pickup_item(current_room):
	global inventory
	
	for k,v in rooms[current_room].items():
		if k == 'Items':

			#inventory["Name"] = item

			for index,item in rooms[current_room]['Items'].items():
				 	for k,v in item.items():
				 		inventory['Name'] = v

					
########################################################

# MAIN
def main():
	# Setup
	welcome()
	current_room = 'Room_1'

	while True:
		game_over(current_room)
		pickup_item(current_room)
		menu_options = build_menu(current_room)
		choice = int(make_choice(current_room, menu_options))
		current_room = update_room(choice, current_room, menu_options)

main()


