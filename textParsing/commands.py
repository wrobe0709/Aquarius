#This file will be used to handle parsing command line
#user input. It will then call on appropriate functions
#from other commands and pass through information as needed
import sys
import csv
import fileinput
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
    print current_room.get_short_description() + "\n"
    print "The room contains the following features"
    for feature in current_room.features:
        print "     " + current_room.features[feature].get_name() + ": ", current_room.features[feature].get_description()
    print "The room contains the following item"
    for item in current_room.items:
        print "     " + current_room.items[item].get_name() + ": ", current_room.items[item].get_description()

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
    if character.get_inventory() == {}:
        print 'Inventory is empty'
    else:
        for item in character.get_inventory():
            print "     " + character.get_inventory()[item].get_name() + ": ", character.get_inventory()[item].get_description()

#This function will add an item to the player's inventory and remove it from the
#game world
def take_item(character, item_key, item):
    """Adds an item to a player's inventory"""
    current_room = character.get_current_room()
    current_room_items = current_room.get_items()
    # Add the item to inventory and remove it from the room
    if current_room_items[item_key]:
        character.add_to_inventory(item_key, item)
        current_room.remove_item(item_key)
    else:
        print "That item doesn't appear to be in this room."

def drop_item(character, item_key):
    """Removes an item from inventory and leaves it in a room"""
    current_room = character.get_current_room()
    current_room.add_item(character.get_inventory()[item_key])
    character.remove_from_inventory(item_key)

#this will probably need some revision...
def change_room(character, game_map, direction):
    """Changes a player's room"""
    usr_choice = getattr(game_map[character.current_room.get_name()], direction)
    current_room = character.get_current_room()
    #make sure it's a valid choice within the game map
    if usr_choice in game_map:
        character.set_potential_room(game_map[usr_choice])
        potential_room = character.get_potential_room()
        #make sure the path isn't locked
        if potential_room.get_locked_status() == 'false':
            character.set_current_room(game_map[usr_choice])
        elif potential_room.get_locked_status() == 'true':
            print "That way seems to be locked at the moment...perhaps there is a way to open it..."
            
    else:
        print "There is no way..."


def save_game(character):
    #Will have to update this later when we figure out what what is to be saved in text file

    """Writes character name, current room & inventory list to textfile"""
    character_name = character.get_name()
    current_room = character.get_current_room().get_name()
    inventory = character.get_inventory()

    with open("output.txt", "w") as text_file:
        text_file.write(character_name + ',')
        text_file.write(current_room + ',')
        text_file.write(','.join(str(i) for i in inventory))

def load_game(character, game_map):
    #Will have to update this later when we figure out what what is to be saved in text file

    """Loads character name, current room & inventory list from textfile"""
    with open("output.txt") as text_file:
        line = text_file.read()
        textList = line.split(',')
        #1st in list is character name
        character.set_name(textList[:1])
        #2nd in list is current room
        character.set_current_room(game_map[textList[1]])
        #3rd - on in list is inventory items
        for item in textList[2:]:
            character.add_to_inventory(item, item)
        #print(textList)


