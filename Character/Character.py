"""Character docstring"""
class Character(object):
    """Character Class"""
    def __init__(self):
        self.name = ''
        self.current_room = ''
    
    def set_name(self, name):
        """Sets the name of a character"""
        self.name = name
    
    def set_current_room(self, current_room):
        """Sets the description of a room"""
        print "\nEntering", current_room.get_name(), "..."
        print current_room.get_short_description()
        self.current_room = current_room

    def get_name(self):
        """Gets the name of a character"""
        return self.name
    
    def get_current_room(self):
        """Gets the current room"""
        return self.current_room
