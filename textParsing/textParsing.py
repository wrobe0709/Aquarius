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
    print "What do you want to do?"
    userCommand = raw_input('> ')
    #print len(userCommand)
    #Separate and store the words in a list
    commandList = userCommand.split(" ")
    #print len(commandList)
    while (len(commandList) < 1) or (len(commandList) > 2):
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
            examineRoom(character)
        #handle location movement commands
        elif commandList[word] == 'go':
            if commandList[word+1] == 'north':
                usr_choice = getattr(game_map[character.current_room.get_name()], commandList[word+1])
                if usr_choice in game_map:
                    character.set_current_room(game_map[usr_choice])
                else:
                    print "There is no way..."
            elif commandList[word+1] == 'south':
                usr_choice = getattr(game_map[character.current_room.get_name()], commandList[word+1])
                if usr_choice in game_map:
                    character.set_current_room(game_map[usr_choice])
                else:
                    print "There is no way..."
            elif commandList[word+1] == 'east':
                usr_choice = getattr(game_map[character.current_room.get_name()], commandList[word+1])
                if usr_choice in game_map:
                    character.set_current_room(game_map[usr_choice])
                else:
                    print "There is no way..."
            elif commandList[word+1] == 'west':
                usr_choice = getattr(game_map[character.current_room.get_name()], commandList[word+1])
                if usr_choice in game_map:
                    character.set_current_room(game_map[usr_choice])
                else:
                    print "There is no way..."
        #handle item manipulation
        elif commandList[word] == 'examine':
            examineItem(character)
        elif commandList[word] == 'pickup':
            grabItem(character)
        elif commandList[word] == 'take':
            grabItem(character)
        elif commandList[word] == 'grab':
            grabItem(character)
        elif commandList[word] == 'help':
            displayHelp()
        elif commandList[word] == 'inventory':
            displayInventory(character)
        elif commandList[word] == 'attack':
            print "You take your weapon and slay the monster."
        elif commandList[word] == 'drop':
            print "You have dropped the <object>"
        elif commandList[word] == 'use':
            print "You used <object>"
        elif commandList[word] == 'quit':
            return 'quit'
