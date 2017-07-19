"""Item docstring"""
class Item(object):
    """Item Class"""
    def __init__(self):
        self.name = ''
        self.description = ''
        self.looked_at = False

    def set_name(self, name):
        """Sets the name of an item"""
        self.name = name

    def set_description(self, description):
        """Sets the name of an item"""
        self.description = description

    def set_looked_at(self, looked_at):
        """Sets the looked_at status of an item"""
        self.looked_at = looked_at

    def get_name(self):
        """Gets the name of an item"""
        return self.name

    def get_description(self):
        """Gets the description of an item"""
        return self.description

    def get_looked_at(self):
        """Gets the looked_at status of an item"""
        return self.looked_at
