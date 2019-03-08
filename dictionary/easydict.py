class EasyDict(dict):
    """Creating dictionaries more easily, e.g. for logging or collecting data"""

    def __missing__(self, key):
        """If key is missing, add it."""
        value = self[key] = type(self)()
        return value