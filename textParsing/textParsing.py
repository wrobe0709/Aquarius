#This file will be used to handle parsing command line
#user input. It will then call on appropriate functions
#from other commands and pass through information as needed
import sys
import csv
from commands import *

#Used for testing user input, update once
#integrated with the player object
def userInput():
    #change this prompt to be situational
    # print "What do you want to do?"
    userCommand = raw_input('> ')
    #print len(userCommand)
    #Separate and store the words in a list
    commandList = userCommand.split(" ")
    #print len(commandList)
    while (len(commandList) < 1) or (len(commandList) > 2):
        # Allow for 3 commands with 'look at'
        if commandList[0] == 'look' and commandList[1] == 'at':
            break
        elif commandList[0] == 'take':
            break
        elif commandList[0] == 'drop':
            break
        else:
            print'''
            Your command input was improper, please use 1 - 2 valid commands.
            Type 'help' to see a list of viable commands. Please try again.
            '''
            userCommand = raw_input()
            #Separate and store the words in a list
            commandList = userCommand.split(" ")

    return commandList


#This function will take the commandList produced by userInput, it will
#then
def handleCommands(commandList, character, game_map):
    #Iterate through the commands and look for keywords to execute commands
    #based on the keywords from the commandList

    for word in range(len(commandList)):
        #first handle file saving & loading
        if commandList[word] == 'save':
            print "Saving game."
        elif commandList[word] == 'load':
            print "Which game would you like to load?"
        #next handle observing the room
        elif commandList[word] == 'look':
            if len(commandList) == 1:
                examine_room(character)
            elif commandList[word+1] == 'at':
                object_key = ''
                for item_word in commandList[2:]:
                        object_key += item_word + ' '
                object_key = object_key[:-1].title()
                # check if is an item
                if object_key in character.get_current_room().get_items():
                    look_at_item(character, object_key)
                # check it is a feature
                elif object_key in character.get_current_room().get_features():
                    look_at_feature(character, object_key)
                else:
                    print "That does not appear to be a feature or object in this room"
            else:
                print "You can either 'look' or 'look at <feature or object>'"
        #handle location movement commands
        elif commandList[word] == 'go':
            if commandList[word+1] == 'north':
                change_room(character, game_map, 'north')
            elif commandList[word+1] == 'south':
                change_room(character, game_map, 'south')
            elif commandList[word+1] == 'east':
                change_room(character, game_map, 'east')
            elif commandList[word+1] == 'west':
                change_room(character, game_map, 'west')
        #handle item manipulation
        #elif commandList[word] == 'examine':
            #look_at_item(character)
        elif commandList[word] == 'pickup':
            if len(commandList) == 1:
                print 'You must specify an item to take with you'
            else:
                item_key = ''
                for item_word in commandList[1:]:
                    item_key += item_word + ' '
                item_key = item_key[:-1].title()
                if item_key in character.get_current_room().get_items():
                    take_item(character, item_key)
        elif commandList[word] == 'take':
            if len(commandList) == 1:
                print 'You must specify an item to take with you'
            else:
                item_key = ''
                for item_word in commandList[1:]:
                    item_key += item_word + ' '
                item_key = item_key[:-1].title()
                if item_key in character.get_current_room().get_items():
                    take_item(character, item_key, character.get_current_room().get_items()[item_key])
        elif commandList[word] == 'grab':
            if len(commandList) == 1:
                print 'You must specify an item to take with you'
            else:
                item_key = ''
                for item_word in commandList[1:]:
                    item_key += item_word + ' '
                item_key = item_key[:-1].title()
                if item_key in character.get_current_room().get_items():
                    take_item(character, item_key)
        elif commandList[word] == 'help':
            display_help()
        elif commandList[word] == 'inventory':
            display_inventory(character)
        elif commandList[word] == 'attack':
            print "You take your weapon and slay the monster."
        elif commandList[word] == 'drop':
            if len(commandList) == 1:
                print 'You must specify an item to drop'
            else:
                item_key = ''
                for item_word in commandList[1:]:
                    item_key += item_word + ' '
                item_key = item_key[:-1].title()
                if item_key in character.get_inventory():
                    drop_item(character, item_key)
                else:
                    print 'That item is not in your inventory'
        elif commandList[word] == 'use':
            if len(commandList) == 1:
                print "You must specify a feature to use/interact with."
            else:
                feature_key = commandList[1].title()
                use_feature(character, feature_key)

        elif commandList[word] == 'quit':
            return 'quit'
