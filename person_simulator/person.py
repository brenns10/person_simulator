"""Holds the Person base class."""


class Person():
    def __init__(self, base_updates=[], interactions=[], **kwargs):
        self._base_updates = base_updates
        self._interactions = []
        for attr, val in kwargs.items():
            self.__dict__[attr] = val

    def get_base_update(self):
        return self._base_updates

    def get_interaction(self):
        return self._interactions
        
