#This file will be used to handle parsing command line
#user input. It will then call on appropriate functions
#from other commands and pass through information as needed
import sys
import csv

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
