#This file will be used to handle parsing command line
#user input. It will then call on appropriate functions
#from other commands and pass through information as needed
import sys
import csv

#Used for testing user input, update once
#integrated with the player object
def userInput():
    #change this prompt to be situational
    print "Imagine that you've read about the currently entered room."
    print "What do you want to do?"
    userCommand = raw_input()
    print len(userCommand)
    #Separate and store the words in a list
    commandList = userCommand.split(" ")
    print len(commandList)
    while (len(commandList) < 1) or (len(commandList) > 4):
         print'''
         Your command input was improper, please use 4 or fewer commands,
         and at least one valid command.
         Type 'help' to see a list of viable commands. Please try again.
         '''
         userCommand = raw_input()
         #Separate and store the words in a list
         commandList = userCommand.split(" ")

    return commandList

#prints out the list of available commands to the user
def displayHelp():
    print '''
            **********************************************************
                                    HELP MENU
                                Viable Commands:
            save or savegame - will save a current session of your game
            load or loadgame - will load a previous game session
            look - shows the description of the room, can be used in
            conjunction with the prepositions noted below to examine
            more of the room
            go (noth, south, east, west) - will move the player to a
            room in that direction if possible
            examine - the player will examine an item already in their
            inventory
            take/grab/pickup <object> - will put the selected item in the
            player's inventory and remove it from the room
            drop <object> - will drop selected item from the player's
            inventory
            help - displays this menu
            attack <opponent> - will use the currently equipped weapon to
            attack the indicated opponent
            use <object> - the player will interact with the object
            --------------------------------------------------------
            Prepositions (used in conjunction with some commands above):
            above - used with look (look above <object>)
            into - used with look (look into <room>)
            on - used with look or drop (look/drop on <object>)
            behind - used with look (look behind <room/object>)
            through - used with look (look through <room/object>)
            under - used with look (look under <object>)
            **********************************************************
            '''
#this function will iterate through and display the player's inventory
#def displayInventory(player):


#This function will take the commandList produced by userInput, it will
#then
def handleCommands(commandList):
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
            print "The longform evaluation of the room will be here."
        #handle location movement commands
        elif commandList[word] == 'go':
            if commandList[word+1] == 'north':
                print "Moving to the northern room."
            elif commandList[word+1] == 'south':
                print "Moving to the southern room."
            elif commandList[word+1] == 'east':
                print "Moving to the eastern room."
            elif commandList[word+1] == 'west':
                print "Moving to the western room."
        #handle item manipulation
        elif commandList[word] == 'examine':
            print "You drawn near the <object> for closer evaluation..."
        elif commandList[word] == 'pickup':
            print "You acquired the <object> from the <room>."
        elif commandList[word] == 'help':
            displayHelp()
        elif commandList[word] == 'inventory':
            print "Inventory as follows: "
            #displayInventory(player)
        elif commandList[word] == 'attack':
            print "You take your weapon and slay the monster."
        elif commandList[word] == 'drop':
            print "You have dropped the <object>"
        elif commandList[word] == 'use':
            print "You used <object>"






#testing below
newCommand = userInput()
handleCommands(newCommand)
