#This file will be used to handle parsing command line
#user input. It will then call on appropriate functions
#from other commands and pass through information as needed
import sys
import csv
import Room.Room as Room
import Character.Character as Character
import Feature.Feature as Feature
import Item.Item as Item



#prints out the list of available commands to the user
def displayHelp():
    print '''
            **********************************************************
                                    HELP MENU
                                Viable Commands:
            save or savegame - will save a current session of your game
            load or loadgame - will load a previous game session
            look - shows the description of the room along with items that
            are currently visible/available in the room
            go (noth, south, east, west) - will move the player to a
            room in that direction if possible
            examine - the player will be offered the chance to examine an
            item in the current room
            take/grab/pickup <object> - will put the selected item in the
            player's inventory and remove it from the room
            drop <object> - will drop selected item from the player's
            inventory
            use <object> - the player will interact with the object
            inventory - will display the items in the player's inventory
            help - displays this menu
            attack <opponent> - will use the currently equipped weapon to
            attack the indicated opponent
            quit - will exit the game
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
#This function will return the short description of the character's current room
#and the items within it
def examineRoom(character):
    currentRoom = character.get_current_room()
    print currentRoom.get_short_description()
    print currentRoom.get_items()

#This function will return the description of the passed through item
def examineItem(character):
    currentRoom = character.get_current_room()
    print "Please enter an item that you would like to examine in the room."
    print "Please note that it's currently case sensitive for items."
    item = raw_input('> ')
    currentRoomItems = currentRoom.get_items()
    if item in currentRoomItems:
        print currentRoomItems[item].get_description()
    else:
        print "That item doesn't appear to be in this room."

#this function will iterate through and display the player's inventory
def displayInventory(character):
    print "Inventory as follows: "
    print character.get_inventroy()

#This function will add an item to the player's inventory and remove it from the
#game world
def grabItem(character):
    print "What item would you like to add to your inventory?"
    item = raw_input('> ')
    currentRoom = character.get_current_room()
    currentRoomItems = currentRoom.get_items()
    if item in currentRoomItems:
        character.add_to_inventory(item)
        currentRoom.remove_item(item)
        #print character.get_inventroy()
    else:
        print "That item doesn't appear to be in this room."

def dropItem(character):
    print "What item from your inventory would you like to drop?"
    item = raw_input('> ')
    if item in character.get_inventroy():
        print "Dropping " + str(item) + "."
        #add in function for character.remove_item
        currentRoom = character.get_current_room()
        currentRoom.add_item(item)
    else:
        print "That doesn't appear to be in your inventory."
