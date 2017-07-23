"""Character docstring"""
class Character(object):
    """Character Class"""
    def __init__(self):
        self.name = ''
        self.current_room = ''
        self.potential_room = ''
        self.inventory = {}

    def set_name(self, name):
        """Sets the name of a character"""
        self.name = name

    def set_current_room(self, current_room):
        """Sets the description of a room"""
        print "\nEntering", current_room.get_name(), "..."
        if current_room.visited is False:
            current_room.set_visited(True)
            print current_room.get_long_description()
        else:
            print current_room.get_short_description()
        print "The room contains the following features"
        for feature in current_room.features:
            print "     " + current_room.features[feature].get_name() + ": ", current_room.features[feature].get_description()
        print "The room contains the following items"
        for item in current_room.items:
            print "     " + current_room.items[item].get_name() + ": ", current_room.items[item].get_description()
        self.current_room = current_room

    def set_potential_room(self, potential_room):
        '''Sets a potential room to check for locked features'''
        self.potential_room = potential_room

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
        '''Returns potential room'''
        return self.potential_room

    def get_inventory(self):
        """Gets the character's inventroy"""
        return self.inventory
