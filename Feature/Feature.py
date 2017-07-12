"""Feature docstring"""
class Feature(object):
    """Feature Class"""
    def __init__(self):
        self.name = ''
        self.description = ''

    def set_name(self, name):
        """Sets the name of an feature"""
        self.name = name

    def set_description(self, description):
        """Sets the name of an feature"""
        self.description = description

    def get_name(self):
        """Gets the name of an feature"""
        return self.name

    def get_description(self):
        """Gets the description of an feature"""
        return self.description
