#This file will be used to handle parsing command line
#user input. It will then call on appropriate functions
#from other commands and pass through information as needed
from commands import *

#Used for testing user input, update once
#integrated with the player object
def user_input():
    """Handles user input"""
    user_command = raw_input('> ')
    command_list = user_command.split(" ")
    return command_list


#This function will take the command_list produced by user_input, it will
#then
def handle_commands(command_list, character, game_map):
    """Handles commands"""
    #Iterate through the commands and look for keywords to execute commands
    #based on the keywords from the command_list
    for word in range(len(command_list)):
        #first handle file saving & loading
        if command_list[word] == 'savegame':
            print "Saving game."
            save_game(character, game_map)
            break
        #next handle observing the room
        elif command_list[word] == 'look':
            if len(command_list) == 1:
                examine_room(character)
            elif command_list[word+1] == 'at':
                object_key = ''
                for item_word in command_list[2:]:
                    object_key += item_word + ' '
                object_key = object_key[:-1].title()
                # check if is an item
                if object_key in character.get_current_room().get_items():
                    look_at_item(character, object_key)
                    break
                # check it is a feature
                elif object_key in character.get_current_room().get_features():
                    look_at_feature(character, object_key)
                    break
                else:
                    print "That does not appear to be a feature or object in this room"
                    break
            else:
                print "You can either 'look' or 'look at <feature or object>'"
                break
        #handle location movement commands
        elif command_list[word] == 'go':
            if len(command_list) == 1:
                print " You must specify a specific direction."
                print " Try 'go <north/south/east/west>' or 'go <adjacent room>'"
                break
            elif command_list[word+1] == 'north':
                change_room(character, game_map, 'north')
                break
            elif command_list[word+1] == 'south':
                change_room(character, game_map, 'south')
                break
            elif command_list[word+1] == 'east':
                change_room(character, game_map, 'east')
                break
            elif command_list[word+1] == 'west':
                change_room(character, game_map, 'west')
                break
            else:
                room_key = ''
                for room_word in command_list[1:]:
                    room_key += room_word + ' '
                room_key = room_key[:-1].title()
                if room_key in character.get_current_room().get_adjacent_rooms():
                    change_room(character, game_map, character.get_current_room().get_adjacent_rooms()[room_key])
                    break
                else:
                    print "That is not an adjacent room"
                    break
        elif command_list[word] == 'north' and command_list[word-1] != 'go':
            change_room(character, game_map, 'north')
            break
        elif command_list[word] == 'south' and command_list[word-1] != 'go':
            change_room(character, game_map, 'south')
            break
        elif command_list[word] == 'east' and command_list[word-1] != 'go':
            change_room(character, game_map, 'east')
            break
        elif command_list[word] == 'west' and command_list[word-1] != 'go':
            change_room(character, game_map, 'west')
            break
        #handle item manipulation
        #elif command_list[word] == 'examine':
            #look_at_item(character)
        elif command_list[word] == 'pickup':
            if len(command_list) == 1:
                print 'You must specify an item to take with you'
                break
            else:
                item_key = ''
                for item_word in command_list[1:]:
                    item_key += item_word + ' '
                item_key = item_key[:-1].title()
                if item_key in character.get_current_room().get_items():
                    take_item(character, item_key, character.get_current_room().get_items()[item_key])
                    break
                else:
                    print "You can't pick that up"
                    break
        elif command_list[word] == 'take':
            if len(command_list) == 1:
                print 'You must specify an item to take with you'
                break
            else:
                item_key = ''
                for item_word in command_list[1:]:
                    item_key += item_word + ' '
                item_key = item_key[:-1].title()
                if item_key in character.get_current_room().get_items():
                    take_item(character, item_key, character.get_current_room().get_items()[item_key])
                    break
                else:
                    print "You can't take that"
                    break
        elif command_list[word] == 'grab':
            if len(command_list) == 1:
                print 'You must specify an item to take with you'
            else:
                item_key = ''
                for item_word in command_list[1:]:
                    item_key += item_word + ' '
                item_key = item_key[:-1].title()
                if item_key in character.get_current_room().get_items():
                    take_item(character, item_key, character.get_current_room().get_items()[item_key])
                    break
                else:
                    print "You can't grab that"
                    break
        elif command_list[word] == 'help':
            display_help()
            break
        elif command_list[word] == 'inventory':
            display_inventory(character)
            break
        elif command_list[word] == 'attack':
            print "You take your weapon and slay the monster."
            break
        elif command_list[word] == 'drop':
            if len(command_list) == 1:
                print 'You must specify an item to drop'
                break
            else:
                item_key = ''
                for item_word in command_list[1:]:
                    item_key += item_word + ' '
                item_key = item_key[:-1].title()
                if item_key in character.get_inventory():
                    drop_item(character, item_key)
                    break
                else:
                    print 'That item is not in your inventory'
                    break
        elif command_list[word] == 'use':
            if len(command_list) == 1:
                print "You must specify a feature to use/interact with."
                break
            else:
                object_key = ''
                for item_word in command_list[1:]:
                    object_key += item_word + ' '
                object_key = object_key[:-1].title()
                # check if is an item
                if object_key in character.get_inventory():
                    use_feature(character, object_key)
                    break
                # check it is a feature
                elif object_key in character.get_current_room().get_features():
                    use_feature(character, object_key)
                    break
                else:
                    print "That does not appear to be a feature or in your inventory"
                    break
        elif command_list[word] == 'quit':
            return 'quit'
        else:
            room_key = ''
            for room_word in command_list:
                room_key += room_word + ' '
            room_key = room_key[:-1].title()
            if room_key in character.get_current_room().get_adjacent_rooms():
                change_room(character, game_map, character.get_current_room().get_adjacent_rooms()[room_key])
                break
            else:
                print "That is not an adjacent room"
                break
