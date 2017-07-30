"""Monster docstring"""
class Monster(object):
    """Monster Class"""
    def __init__(self):
        self.name = ''
        self.lvl = ''
        self.description = ''
        self.defeated = False

    def set_name(self, name):
        """Sets the monster name"""
        self.name = name

    def set_lvl(self, lvl):
        """Sets the monster level"""
        self.lvl = lvl

    def set_description(self, description):
        """Sets the monster description"""
        self.description = description

    def get_name(self):
        """Gets the monster name"""
        return self.name

    def get_lvl(self):
        """Gets the monster level"""
        return self.lvl

    def get_description(self):
        """Gets the monster description"""
        return self.description

    def set_defeated_status(self, defeated):
        """Sets the status of the monster"""
        self.defeated = defeated

    def get_defeated_status(self):
        """Gets the status of the monster"""
        return self.defeated
