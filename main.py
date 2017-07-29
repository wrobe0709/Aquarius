"""Aquarius docstring"""
import Room.Room as Room
import Character.Character as Character
import Feature.Feature as Feature
import Item.Item as Item
import constants
from textParsing.textParsing import handle_commands, user_input, load_game

def create_map(json_game_map):
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

        # If it is not a loaded game
        if not json_game_map:
            # Set items in the room
            for item in constants.ROOMS[room]['items']:
                new_item = Item.Item()
                new_item.set_name(constants.ROOMS[room]['items'][item]['name'])
                new_item.set_description(constants.ROOMS[room]['items'][item]['description'])
                if "hidden" in constants.ROOMS[room]['items'][item]:
                    if constants.ROOMS[room]['items'][item]["hidden"] == "true":
                        new_item.set_hidden(True)
                room_hash[room].add_item(new_item)
        # If it is a loaded game
        else:
            # Set items in the room
            for item in json_game_map[room]:
                new_item = Item.Item()
                new_item.set_name(json_game_map[room][item]['Name'])
                new_item.set_description(json_game_map[room][item]['Description'])
                if "Hidden" in json_game_map[room][item]:
                    if json_game_map[room][item]["Hidden"]:
                        new_item.set_hidden(True)
                room_hash[room].add_item(new_item)
   
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
        game_map = create_map(None)
        
        # Setup the starting room
        current_room = game_map['Dungeon Entrance']
        
        # Setup the character
        character_name = raw_input('Enter character name > ')
        character.set_name(character_name)
        character.set_current_room(current_room)

    elif game_start == '2':
        # Initialize character and map
        character = Character.Character()
        saved_game_data = load_game()
        game_map = create_map(saved_game_data['json_game_map'])

        # Set current room and character name based on saved JSON
        current_room = game_map[saved_game_data['current_room']]
        character_name = saved_game_data['character_name']
        character.set_name(character_name)
        character.set_current_room(current_room)

        # Add correct items to inventory
        for item in saved_game_data['json_inventory']:
            new_item = Item.Item()
            new_item.set_name(saved_game_data['json_inventory'][item]['Name'])
            new_item.set_description(saved_game_data['json_inventory'][item]['Description'])
            character.add_to_inventory(item, new_item)

    #handle commands
    new_command = user_input()
    while new_command != 'quit':
        handle_commands(new_command, character, game_map)
        new_command = user_input()

if __name__ == '__main__':
    main()
