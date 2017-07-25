"""Aquarius docstring"""
import Room.Room as Room
import Character.Character as Character
import Feature.Feature as Feature
import Item.Item as Item
import constants
from TextParsing.TextParsing import *

def create_map():
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

        for item in constants.ROOMS[room]['items']:
            new_item = Item.Item()
            new_item.set_name(constants.ROOMS[room]['items'][item]['name'])
            new_item.set_description(constants.ROOMS[room]['items'][item]['description'])
            room_hash[room].add_item(new_item)

    return room_hash

def main():
    """Execution of Aquarius Game"""
    # Create the game map
    game_map = create_map()

    # Setup the starting room
    current_room = game_map['Dungeon Entrance']

    # Setup the character
    character = Character.Character()
    character_name = raw_input('Enter character name > ')
    character.set_name(character_name)
    character.set_current_room(current_room)

    #handle commands
    new_command = user_input()
    while new_command != 'quit':
        handle_commands(new_command, character, game_map)
        new_command = user_input()




if __name__ == '__main__':
    main()
