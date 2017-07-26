"""Aquarius docstring"""
import Room.Room as Room
import Character.Character as Character
import Feature.Feature as Feature
import Item.Item as Item
import constants
from TextParsing.textParsing import *

def create_map(loaded_game, character):
    """Creates map for Aquarius Game"""
    room_hash = {}

    for room in constants.ROOMS:
        # Set name, description, and neighbors
        room_hash[room] = Room.Room()
        room_hash[room].set_name(room)
        room_hash[room].set_short_description(constants.ROOMS[room]['short_description'])
        room_hash[room].set_long_description(constants.ROOMS[room]['long_description'])
        room_hash[room].set_north(constants.ROOMS[room]['north'])
        room_hash[room].set_south(constants.ROOMS[room]['south'])
        room_hash[room].set_east(constants.ROOMS[room]['east'])
        room_hash[room].set_west(constants.ROOMS[room]['west'])
        room_hash[room].set_locked(constants.ROOMS[room]['locked'])

        # Set features in the room
        for feature in constants.ROOMS[room]['features']:
            new_feature = Feature.Feature()
            new_feature.set_name(constants.ROOMS[room]['features'][feature]['name'])
            new_feature.set_description(constants.ROOMS[room]['features'][feature]['description'])
            room_hash[room].add_feature(new_feature)

        if not loaded_game:
            # Set items in the room
            for item in constants.ROOMS[room]['items']:
                new_item = Item.Item()
                new_item.set_name(constants.ROOMS[room]['items'][item]['name'])
                new_item.set_description(constants.ROOMS[room]['items'][item]['description'])
                room_hash[room].add_item(new_item)
        else:
            # Set items in the room
            for item in constants.ROOMS[room]['items']:
                # If the item is not in the player's inventory then add it to the room as normal
                if item not in character.get_inventory():
                    new_item = Item.Item()
                    new_item.set_name(constants.ROOMS[room]['items'][item]['name'])
                    new_item.set_description(constants.ROOMS[room]['items'][item]['description'])
                    room_hash[room].add_item(new_item)
                # Otherwise create the item object and add it to inventory
                else:
                    new_item = Item.Item()
                    new_item.set_name(constants.ROOMS[room]['items'][item]['name'])
                    new_item.set_description(constants.ROOMS[room]['items'][item]['description'])
                    character.add_to_inventory(item, new_item)

    return room_hash

def main():
    """Execution of Aquarius Game"""

    # Welcome character
    print "Welcome to The Aquarius Adventure Game!"
    print " 1.) Start a new game"
    print " 2.) Load a game"
    game_start = raw_input('> ')
    while game_start != '1' and game_start != '2':
        print " Please choose 1 or 2"
        game_start = raw_input('> ')

    if game_start == '1':
        # Initialize character and map
        character = Character.Character()
        game_map = create_map(False, character)
        
        # Setup the starting room
        current_room = game_map['Dungeon Entrance']
        
        # Setup the character
        character_name = raw_input('Enter character name > ')
        character.set_name(character_name)
        character.set_current_room(current_room)

    elif game_start == '2':
        # Initialize character and map
        character = Character.Character()
        load_game(character)

        # # Load items first so game map can be build correctly
        # load_items(character)
        # game_map = create_map(True, character)

        # # Load character name and current room
        # load_character_name(character)
        # load_character_current_room(character, game_map)
        # print character.get_name()
        
        
        
        # print "loading a fake game with:"
        # print " start room = great_hall"
        # print " name = Thomas"
        # # Setup the starting room
        # current_room = game_map['Great Hall']
        
        # # Setup character
        # character = Character.Character()
        # character_name = 'Thomas'
        # character.set_name(character_name)
        # character.set_current_room(current_room)

    #handle commands
    new_command = user_input()
    while new_command != 'quit':
        handle_commands(new_command, character, game_map)
        new_command = user_input()

if __name__ == '__main__':
    main()
