"""Aquarius docstring"""
import Room.Room as Room
import Character.Character as Character
import Feature.Feature as Feature
import Item.Item as Item
import Monster.Monster as Monster
import constants
from textParsing.textParsing import handle_commands, user_input, load_game
from textParsing.puzzles import *
from companionText import *

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

        #Set monsters in the room
        for monster in constants.ROOMS[room]['monsters']:
            if constants.ROOMS[room]['monsters'] != "None":
                new_monster = Monster.Monster()
                new_monster.set_name(constants.ROOMS[room]['monsters'][monster]['name'])
                new_monster.set_lvl(constants.ROOMS[room]['monsters'][monster]['lvl'])
                new_monster.set_description(constants.ROOMS[room]['monsters'][monster]['description'])
                room_hash[room].add_monster(new_monster)

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
                if item == "visited":
                    room_hash[room].set_visited(json_game_map[room][item])
                elif item == "locked":
                    room_hash[room].set_locked(json_game_map[room][item])
                else:
                    new_item = Item.Item()
                    new_item.set_name(json_game_map[room][item]['Name'])
                    new_item.set_description(json_game_map[room][item]['Description'])
                    if "Hidden" in json_game_map[room][item]:
                        if json_game_map[room][item]["Hidden"]:
                            new_item.set_hidden(True)
                    room_hash[room].add_item(new_item)
    return room_hash

def play_game():
    """Execution of Aquarius Game"""

    # Welcome character
    game_start = game_menu()
    while game_start != 'newgame' and game_start != 'loadgame':
        if game_start == 'walkthrough':
            game_walkthrough()
        print " Please enter newgame, loadgame, or walkthrough"
        game_start = game_menu()

    if game_start == 'newgame':
        # Initialize character and map
        character = Character.Character()
        game_intro()
        game_map = create_map(None)

        # Setup the starting room
        current_room = game_map['Dungeon Entrance']

        # Setup the character
        character_name = raw_input('Enter character name > ')
        character.set_name(character_name)
        character.set_current_room(current_room)
        character.set_game_map(game_map)

    elif game_start == 'loadgame':
        # Initialize character and map
        character = Character.Character()
        saved_game_data = load_game()
        game_map = create_map(saved_game_data['json_game_map'])

        # Set current room and character name based on saved JSON
        current_room = game_map[saved_game_data['current_room']]
        character_name = saved_game_data['character_name']
        character.set_name(character_name)
        character.set_current_room(current_room)
        character.set_game_map(game_map)

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
