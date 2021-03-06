from textParsing.puzzles import *
"""Character docstring"""
class Character(object):
    """Character Class"""
    def __init__(self):
        self.name = ''
        self.current_room = ''
        self.potential_room = ''
        self.inventory = {}
        self.game_map = ''

    def set_name(self, name):
        """Sets the name of a character"""
        self.name = name

    def set_current_room(self, current_room):
        """Sets the description of a room"""
        print "\nEntering", current_room.get_name(), "...\n"
        if current_room.visited is False:
            if current_room.get_name() == "Gear Room":
                gear_room_puzzle(self)
            current_room.set_visited(True)
            print current_room.get_long_description(), "\n"
        else:
            print current_room.get_short_description(), "\n"
        print "The room contains the following features"
        for feature in current_room.features:
            print "     " + current_room.features[feature].get_name()
        if len(current_room.items) > 0:
            visible_items = False
            for item in current_room.items:
                if not current_room.items[item].get_hidden():
                    visible_items = True
            if visible_items:
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
                print "The room contains the following monsters"
                for monster in current_room.monsters:
                    if not current_room.monsters[monster].get_defeated_status():
                        print "     " + current_room.monsters[monster].get_name()
        self.current_room = current_room

    def set_potential_room(self, potential_room):
        """Sets a potential room to check for locked features"""
        self.potential_room = potential_room

    def set_game_map(self, game_map):
        """Sets game map"""
        self.game_map = game_map

    def add_to_inventory(self, item_key, item):
        """Adds an item to inventory"""
        self.inventory[item_key] = item

    def remove_from_inventory(self, item):
        """Removes an item to the room"""
        del self.inventory[item]

    def get_name(self):
        """Gets the name of a character"""
        return self.name

    def get_current_room(self):
        """Gets the current room"""
        return self.current_room

    def get_potential_room(self):
        """Returns potential room"""
        return self.potential_room

    def get_inventory(self):
        """Gets the character's inventroy"""
        return self.inventory

    def get_game_map(self):
        """Gets the game map"""
        return self.game_map


