import json
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
            look at <feature/object> - shows description of feature/item
            go (noth, south, east, west, or <room name>) - will move the player
            to a room in that direction if possible, or into the designated room
            examine <item>- the player examines an item in the current room
            take/grab/pickup <object> - will put the selected item in the
            player's inventory and remove it from the room
            drop/discard <object> - will drop the selected item from the
            player's inventory
            use <object> - the player will interact with the object
            inventory - will display the items in the player's inventory
            help - displays this menu
            smash/break - will smash or break open certain items in the
            game world
            read <item>/<feature> - will read an item in the player's inventory
            or a feature in the room
            flip - will flip a certain feature between on and off
            quit - will exit the game
            **********************************************************

            '''

def examine_room(character):
    """Examine a room"""
    current_room = character.get_current_room()
    print current_room.get_short_description() + "\n"
    print "The room contains the following features"
    for feature in current_room.features:
        print "     " + current_room.features[feature].get_name()
    if len(current_room.items) > 0:
        print "The room contains the following items"
        for item in current_room.items:
            if not current_room.items[item].get_hidden():
                print "     " + current_room.items[item].get_name()
    if len(current_room.monsters) > 0:
        contains_monster = False
        for monster in current_room.monsters:
            if not current_room.monsters[monster].get_defeated_status():
                contains_monster = True
        if contains_monster:
            print "The room contains the following monsters", len(current_room.monsters)
            for monster in current_room.monsters:
                if not current_room.monsters[monster].get_defeated_status():
                    print "     " + current_room.monsters[monster].get_name()

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
        print ' Inventory is empty'
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
                    battle(game_map[usr_choice], character)
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
        if object_key == 'Painting':
            print " The painting is of someone closely examining a key..."
        elif object_key == 'Closet':
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
            change_room(character, character.get_game_map(), 'north')
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
            print " You look into the mirror and see yourself battling a great and mighty floating skeleton!"
            print " Is this a sign of things yet to come?"
        elif object_key == 'Torches':
            print " You attempt to grab a torch from the wall but unable to loosen it."
            print " Perhaps the blue torch can be used..."
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
                print " The puzzle has already been solved"
        elif object_key == 'Door':
            if "End Room Key" in character.get_inventory():
                print " You used the End Room Key to enter the room!"
                change_room(character, character.get_game_map(), 'south')
            else:
                print " The door is locked. There must be a key to unlock it..."
        elif object_key == 'Weapons':
            print " You dig through a pile of old rusted shields, swords, and helmets."
            print " These items are of no use but maybe new ones can be found..."
        elif object_key == 'Keyhole':
            if "End Room Key" in character.get_inventory():
                print " You used the End Room Key to enter the room!"
                change_room(character, character.get_game_map(), 'south')
            else:
                print " You don't have the key to use with this door..."
        elif object_key == 'Barrel 1':
            if 'Helmet' in character.get_game_map()['Barrel Room'].get_items():
                if character.get_game_map()['Barrel Room'].get_items()['Helmet'].get_hidden():
                    print " You smash Barrel 1 and see a shiny new helmet inside."
                    character.get_game_map()['Barrel Room'].get_items()['Helmet'].set_hidden(False)
                else:
                    print " You've already smashed Barrel 1. Did you take the helmet from inside?"
            else:
                print " You've already smashed Barrel 1. Did you take the helmet from inside?"
        elif object_key == 'Barrel 2':
            if 'Shield' in character.get_game_map()['Barrel Room'].get_items():
                if character.get_game_map()['Barrel Room'].get_items()['Shield'].get_hidden():
                    print " You smash Barrel 2 and see a shiny new shield inside."
                    character.get_game_map()['Barrel Room'].get_items()['Shield'].set_hidden(False)
                else:
                    print " You've already smashed Barrel 2. Did you take the shield from inside?"
            else:
                print " You've already smashed Barrel 2. Did you take the shield from inside?"
        elif object_key == 'Quiver':
            print " It's an old quiver left by a past warrior to hold arrows. Arrows would be helpful to a bow..."
        elif object_key == 'Chair':
            if not current_room.get_features()['Chair'].get_interacted_with():
                print " You move the chair near the wall in order to stand on it."
                current_room.get_features()['Chair'].set_interacted_with(True)
            else:
                print   " You already moved the chair. It's up against the wall maybe there's a switch you can reach now..."
        elif object_key == 'Switch':
            if not current_room.get_features()['Chair'].get_interacted_with():
                print " You can't reach the switch. Maybe you can move something in the room and stand on it..."
            else:
                print " Flipping the switch unlocks a door on the south wall."
                character.get_game_map()['Barrel Room'].set_locked("false")
        elif object_key == 'Wizard':
            if not current_room.get_features()['Wizard'].get_interacted_with():
                print " The magestic wizard has refurbished the dungeon into a beatiful palace!"
                current_room.get_features()['Wizard'].set_interacted_with(True)
            else:
                print " The wizard did is job."
        elif object_key == 'Puzzle':
            gear_room_puzzle(character)
        elif object_key == 'Passageway':
            if character.get_game_map()['Bow Room'].get_locked_status() != "false":
                print " The passageway is locked. Maybe solving the puzzle will let you pass..."
            else:
                change_room(character, character.get_game_map(), 'south')
        elif object_key == 'Skeleton Pile':
            print " Examining the skeleton pile further you notice none of the skeletons were wearing a helmet..."
        elif object_key == 'Skeleton':
            print " A closer look at the skeleton and you notice his helmet but he is missing a shield..."
        elif object_key == 'Black Tome':
            print "Flipping through the pages of the Black Tome there are many drawings that look like they're for a summoning ritual of some sort."
        elif object_key == 'Red Tome':
            print "This Tome seems to have ancient writings and drawings that involve human sacrifice, you quickly close it."
        elif object_key == 'Monster':
            print "You use monster"
        elif object_key == 'Ceiling Skylight':
            print " You gaze through the ceiling skylight and see a turret to the east. There must be another room to the east..."
        elif object_key == 'Leak':
            print " Looking at the leak closer you realize the liquid is blood. It's coming from a door on the north wall."
            print " Might not be safe to go that way without the proper equipmnt..."
        elif object_key == 'Odd Book':
            print " You open the book and don't see much. The only thing worthwhile you find is a hint."
            print " It reads: to the north do not go, unless sword and bow are in tow..."
        elif object_key == 'Map':
            print " The map has rotted away a bit but you can make out the basics."
            print " To get to the final room you'll need to be south of your current location..."
        elif object_key == 'Scroll':
            print " The scroll cointains a strange message:"
            print " To slay the beast you'll need the the weapon from the room farthest to the east..."
        elif object_key == 'Broken Armor':
            print " There are only broken pieces of the armor left. It looks like it was used in a batlle recently..."
        elif object_key == 'Broken Sword':
            print " By examining the sword it is clear the warrior had given their best effort to win its battle."
            print " Perhaps the warrior did not have anything to shield itself from its attackers blows..."
    elif object_key in character.get_inventory():
        if object_key == 'Torch':
            print " You pull out and light your torch, and the room fills with light."
            if "Lantern" in current_room.get_features():
                print " You light the lantern with your torch."
        elif object_key == 'Arrows':
            if 'Bow' in character.get_inventory():
                print " You pull out an arrow and notch it in your bow."
            else:
                print " This would be a lot more useful with a bow..."
        elif object_key == 'Sword':
            print "You unsheath your sword and ready yourself for what may lie ahead."
        elif object_key == 'Bow':
            if 'Arrows' in character.get_inventory() and 'Torch Corridor' in current_room:
                print " You pull out your bow and some arrows, you light an arrow with the flame from the blue torch and loose an arrow into the gaseous room."
                if not character.get_game_map()['Gaseous Room'].get_visited():
                    gaseous_room_entry(character)
                else:
                    print " You already used the blue torch to clear the gaseous chamber."
            elif 'Arrows' in character.get_inventory():
                print " You loose an arrow in the room, too bad a monster didn't get hit."
            else:
                print "This would be a lot more useful with arrows, I wonder if I missed those somewhere I've already been..."
        elif object_key == 'Armor Suit':
            print " You put on the piece of armor, it's quite comfortable and exudes power."
        elif object_key == 'Helmet':
            print " You place the helm on your head, you feel ready to take on whatever's next!"
        elif object_key == 'Shield':
            print " The sheild slides onto your arm, it'll definitely help you take on some tough opponents."
        elif object_key == 'Rune':
            if 'Sword' in character.get_inventory():
                print """
                Taking the rune and pulling your sword out, the rune seems to pulse with energy, as it draws near
                the sword the pulsing increases and it's form liquifies. Then the rune melds into the sword! Your
                sword now pulses with the energy of the rune!"""
            else:
                print " This could be of use with the sword..."
        elif object_key == 'Key':
            if current_room == 'Armory':
                print " You used the End Room Key to enter the room!"
                change_room(character, character.get_game_map(), 'south')
            else:
                print "This key has a use, just not here..."
    else:
        print "That feature does not appear to be in this room or is not in inventory"

def read_something(character, object_key):
    """Attempts to read a feature or inventory item"""
    current_room = character.get_current_room()
    if object_key in current_room.get_features():
        if object_key == 'Red Tome':
            print "This Tome seems to have ancient writings and drawings that involve human sacrifice, you quickly close it."
        elif object_key == 'Black Tome':
            print "Flipping through the pages of the Black Tome there are many drawings that look like they're for a summoning ritual of some sort."
        elif object_key == 'Map':
            print "You examine the map closely, it's of the surrounding woods and the castle. The castle seems quite large."
        elif object_key == 'Scroll':
            print " The scroll cointains a strange message:"
            print " To slay the beast you'll need the the weapon from the room farthest to the east..."
        elif object_key == 'Odd Book':
            print " You open the book and don't see much. The only thing worthwhile you find is a hint."
            print " It reads: to the north do not go, unless sword and bow are in tow..."
        else:
            print "You can't really read that, perhaps using it would prove more fruitful."
    elif object_key in character.get_inventory():
        print "You can't really read that, perhaps using it would prove more fruitful."
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
        #Add correct monsters to rooms (if they have not been defeated)
        for monster in game_map[room].get_monsters():
            if not game_map[room].get_monsters()[monster].get_defeated_status():
                json_game_map[room_name][monster] = {
                    'Name': game_map[room].get_monsters()[monster].get_name(),
                    'Lvl':  game_map[room].get_monsters()[monster].get_lvl(),
                    'Description': game_map[room].get_monsters()[monster].get_description(),
                    'Defeated': game_map[room].get_monsters()[monster].get_defeated_status(),
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
