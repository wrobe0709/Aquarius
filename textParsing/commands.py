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
def display_help():
    """Display help menu"""
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
def examine_room(character):
    """Examine a room"""
    current_room = character.get_current_room()
    print current_room.get_short_description()
    print current_room.get_items()

#This function will return the description of the passed through item
def look_at_item(character, item):
    """Look at an item"""
    current_room = character.get_current_room()
    current_room_items = current_room.get_items()
    if current_room_items[item]:
        print ' ' + current_room_items[item].get_description()
        if not current_room_items[item].get_looked_at():
            current_room_items[item].set_looked_at(True)
    else:
        print "That item doesn't appear to be in this room."

#This function will return the description of the passed through feature
def look_at_feature(character, feature):
    """Look at a feature"""
    current_room = character.get_current_room()
    current_room_features = current_room.get_features()
    if current_room_features[feature]:
        print ' ' + current_room_features[feature].get_description()
        if not current_room_features[feature].get_looked_at():
            current_room_features[feature].set_looked_at(True)
    else:
        print "That item doesn't appear to be in this room."

#this function will iterate through and display the player's inventory
def display_inventory(character):
    """Display a player's inventory"""
    print "Inventory as follows: "
    print character.get_inventroy()

#This function will add an item to the player's inventory and remove it from the
#game world
def grab_item(character):
    """Adds an item to a player's inventory"""
    print "What item would you like to add to your inventory?"
    item = raw_input('> ')
    current_room = character.get_current_room()
    current_room_items = current_room.get_items()
    if item in current_room_items:
        character.add_to_inventory(item)
        current_room.remove_item(item)
        #print character.get_inventroy()
    else:
        print "That item doesn't appear to be in this room."

def drop_item(character):
    """Removes an item from """
    print "What item from your inventory would you like to drop?"
    item = raw_input('> ')
    if item in character.get_inventroy():
        print "Dropping " + item + "."
        #add in function for character.remove_item
        current_room = character.get_current_room()
        current_room.add_item(item)
    else:
        print "That doesn't appear to be in your inventory."

def changeRoom(character, game_map, direction):
    usr_choice = getattr(game_map[character.current_room.get_name()], direction)
    if usr_choice in game_map:
        character.set_current_room(game_map[usr_choice])
    else:
        print "There is no way..."
