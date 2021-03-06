"""Room docstring"""
class Room(object):
    """Room Class"""
    def __init__(self):
        self.name = ''
        self.short_description = ''
        self.long_description = ''
        self.north = ''
        self.south = ''
        self.east = ''
        self.west = ''
        self.locked = ''
        self.visited = False
        self.monsters = {}
        self.features = {}
        self.items = {}

    def set_name(self, name):
        """Sets the name of a room"""
        self.name = name

    def set_long_description(self, long_description):
        """Sets the description of a room"""
        self.long_description = long_description

    def set_short_description(self, short_description):
        """Sets the description of a room"""
        self.short_description = short_description

    def set_north(self, north):
        """Sets the north neighbor of a room"""
        self.north = north

    def set_south(self, south):
        """Sets the north neighbor of a room"""
        self.south = south

    def set_east(self, east):
        """Sets the north neighbor of a room"""
        self.east = east

    def set_west(self, west):
        """Sets the north neighbor of a room"""
        self.west = west

    def set_locked(self, locked):
        """Sets the locked status of the room"""
        self.locked = locked

    def set_visited(self, visited):
        """Sets the room as visited"""
        self.visited = visited

    def add_monster(self, monster):
        """Adds a monster to the room"""
        self.monsters[monster.get_name()] = monster

    def add_feature(self, feature):
        """Adds a feature to the room"""
        self.features[feature.get_name()] = feature

    def add_item(self, item):
        """Adds an item to the room"""
        self.items[item.get_name()] = item

    def remove_item(self, item):
        """Removes an item to the room"""
        del self.items[item]

    def get_north(self):
        """Gets the north neighbor of a room"""
        return self.north

    def get_south(self):
        """Gets the south neighbor of a room"""
        return self.south

    def get_east(self):
        """Gets the east neighbor of a room"""
        return self.east

    def get_west(self):
        """Gets the west neighbor of a room"""
        return self.west

    def get_locked_status(self):
        """Returns the locked state of the room"""
        return self.locked

    def get_name(self):
        """Gets the name of a room"""
        return self.name

    def get_long_description(self):
        """Gets the long description of a room"""
        return self.long_description

    def get_short_description(self):
        """Gets the short description of a room"""
        return self.short_description

    def get_visited(self):
        """Gets if a room is visited"""
        return self.visited

    def get_features(self):
        """Gets if a room is visited"""
        return self.features

    def get_items(self):
        """Gets items in a room"""
        return self.items

    def get_adjacent_rooms(self):
        """Gets the room's adjacent rooms"""
        return {
            self.get_north(): "north",
            self.get_south(): "south",
            self.get_east(): "east",
            self.get_west(): "west"
        }
    
    def get_monsters(self):
        """Gets the monsters in a room"""
        return self.monsters
