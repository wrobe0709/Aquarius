"""Room docstring"""
class CurrentRoom(object):
    """CurrentRoom Class"""
    def __init__(self):
        self.name = ''
        self.description = ''
        self.north = ''
        self.south = ''
        self.east = ''
        self.west = ''
    
    def set_name(self, name):
        """Sets the name of a room"""
        self.name = name
    
    def set_description(self, description):
        """Sets the description of a room"""
        self.description = description
    
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
    
    def get_name(self):
        """Gets the name of a room"""
        return self.name
    
    def get_description(self):
        """Gets the description of a room"""
        return self.description

class Neighbor(CurrentRoom):
    """Neighbor Class"""
    def __init__(self):
        super(Neighbor, self).__init__()       
        self.far_off_description = ''

    def set_far_off_description(self, far_off_description):
        """Sets the description of a room"""
        self.far_off_description = far_off_description
    
    def get_far_off_description(self):
        """Gets the description of a room"""
        return self.far_off_description

