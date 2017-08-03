import json
import Room.Room as Room
import Character.Character as Character
import Feature.Feature as Feature
import Item.Item as Item
import Monster.Monster as Monster
from puzzles import *
from battle import *

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

def examine_room(character):
    """Examine a room"""
    current_room = character.get_current_room()
    print current_room.get_short_description() + "\n"
    print "The room contains the following features"
    for feature in current_room.features:
        print "     " + current_room.features[feature].get_name() + ": ", current_room.features[feature].get_description()
    print "The room contains the following item"
    for item in current_room.items:
        if not current_room.items[item].get_hidden():
            print "     " + current_room.items[item].get_name() + ": ", current_room.items[item].get_description()
    print "The room contains the following monsters"
    for monster in current_room.monsters:
        print "     " + current_room.monsters[monster].get_name() + ": ", current_room.monsters[monster].get_description()

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

def display_inventory(character):
    """Display a player's inventory"""
    if character.get_inventory() == {}:
        print 'Inventory is empty'
    else:
        for item in character.get_inventory():
            print "     " + character.get_inventory()[item].get_name() + ": ", character.get_inventory()[item].get_description()

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

def change_room(character, game_map, direction):
    """Changes a player's room"""
    usr_choice = getattr(game_map[character.current_room.get_name()], direction)
    # Check for valid choice
    if usr_choice in game_map:
        character.set_potential_room(game_map[usr_choice])
        potential_room = character.get_potential_room()
        # Check for unlocked route
        if potential_room.get_locked_status() == 'false':
            character.set_current_room(game_map[usr_choice])
            battle(game_map[usr_choice], character)
        elif potential_room.get_locked_status() == 'true':
            if potential_room.get_name() == "End Room":
                if 'End Room Key' in character.get_inventory():
                    character.set_current_room(game_map[usr_choice])
                else:
                    print " That way seems to be locked at the moment...perhaps there is a way to open it..."
            else:
                print " That way seems to be locked at the moment...perhaps there is a way to open it..."
    else:
        print "There is no way..."

# Need to add in a way to handle whether or not the feature has been used before
def use_feature(character, object_key):
    """Uses a feature"""
    current_room = character.get_current_room()
    if object_key in current_room.get_features():
        # Go through and handle the various differing features
        if object_key == 'Closet':
            if "Arrows" in current_room.get_items():
                current_room.get_items()['Arrows'].set_hidden(False)
                print " You see some arrows, these might be of use later..."
            else:
                print " The closet is empty"
        elif object_key == 'Lantern':
            if 'Torch' in character.get_inventory():
                print " You light the lantern with your torch."
            else:
                print " This looks like it could be lit with a torch."
        elif object_key == 'Staircase':
            print " You descend the staircase."
        elif object_key == 'Skylight':
            print " You stare up at the skylight and see light from the moon gently lighting the room."
        elif object_key == 'Display Case':
            if "Sword" in current_room.get_items():
                print " There is a sword in the display case. You must solve the riddle to gake it out."
                sword_case_puzzle(character)
            else:
                print " The display case is empty"
        elif object_key == 'Mirrors':
            print "You look at yourself in a mirror and check out your inventory: "
            display_inventory(character)
        elif object_key == 'Small Mirror':
            print " You look into the mirror and see yourself battling a great and mighty beast!"
            print " Is this a sign of things yet to come?"
        elif object_key == 'Torches':
            print " The torches are all light and burning bright...you feel drawn towards the blue one..."
        elif object_key == 'Blue Torch':
            if not character.get_game_map()['Gaseous Room'].get_visited():
                gaseous_room_entry(character)
            else:
                print " You already used the blue torch to clear the gaseous chamber."
        elif object_key == 'Puzzle Case':
            if "End Room Key" in current_room.get_items():
                if current_room.get_items()["End Room Key"].get_hidden():
                    key_puzzle(character)
                else:
                    print "The puzzle has already been solved"
            else:
                print "The puzzle has already been solved"
        elif object_key == 'Door':
            print "You use the door"
        elif object_key == 'Weapons':
            print "You use the weapons"
        elif object_key == 'Keyhole':
            print "You use the keyhole"
        elif object_key == 'Barrel 1':
            print "You use barrel 1"
        elif object_key == 'Barrel 2':
            print "You use barrel 2"
        elif object_key == 'Quiver':
            print "You use quiver"
        elif object_key == 'Chair':
            print "You use chair"
        elif object_key == 'Switch':
            print "You use switch"
        elif object_key == 'Diamonds':
            print "You use diamonds"
        elif object_key == 'Wizard':
            print "You use wizard"
        elif object_key == 'Boss':
            print "You use boss"
        elif object_key == 'Puzzle':
            gear_room_puzzle(character)
        elif object_key == 'Puzzle Case':
            print "You use puzzle case"
        elif object_key == 'Passageway':
            print "You use passageway"
        elif object_key == 'Skeleton Pile':
            print "You use skeleton pile"
        elif object_key == 'Skeleton':
            print "You use skeleton"
        elif object_key == 'Black Tome':
            print "You use black tome"
        elif object_key == 'Red Tome':
            print "You use red tome"
        elif object_key == 'Monster':
            print "You use monster"
        elif object_key == 'Ceiling Skylight':
            print "You use ceiling skylight"
        elif object_key == 'Leak':
            print "You use leak"
        elif object_key == 'Odd Book':
            print "You use odd book"
    elif object_key in character.get_inventory():
        print "use the", object_key
    else:
        print "That feature does not appear to be in this room or is not in inventory"

def save_game(character, game_map):
    """Save a game to JSON"""
    # Get character info
    character_name = character.get_name()
    current_room = character.get_current_room().get_name()
    inventory = character.get_inventory()

    # Initialize json to save map and inventory
    json_game_map = {}
    json_inventory = {}

    # Add correct items to rooms
    for room in game_map:
        room_name = game_map[room].get_name()
        json_game_map[room_name] = {}
        json_game_map[room_name]["locked"] = game_map[room].get_locked_status()
        json_game_map[room_name]["visited"] = game_map[room].get_visited()
        for item in game_map[room].get_items():
            json_game_map[room_name][item] = {
                'Name': game_map[room].get_items()[item].get_name(),
                'Description': game_map[room].get_items()[item].get_description(),
                'Hidden': game_map[room].get_items()[item].get_hidden()
            }

    # Add items to inventory
    for item in inventory:
        json_inventory[item] = {
            'Name': inventory[item].get_name(),
            'Description': inventory[item].get_description(),
            'Hidden': inventory[item].get_hidden()
        }

    # Create game state object to save
    game_state = {
        "character_name": character_name,
        "current_room": current_room,
        "json_inventory": json_inventory,
        "json_game_map": json_game_map
    }

    # Save the game to a JSON file
    with open('saved_game.json', 'w') as out:
        json.dump(game_state, out)

def load_game():
    """Loads data"""
    with open("saved_game.json") as saved_game_file:
        game_data = json.load(saved_game_file)
    return game_data
