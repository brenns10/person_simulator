"""Holds the Person base class."""
from uuid import uuid4 as generate_uuid

class Person():
    def __init__(self, name, base_updates=[], interactions=[], **kwargs):
        self._id = generate_uuid()
        self._name = name
        self._base_updates = base_updates
        self._interactions = interactions
        for attr, val in kwargs.items():
            self.__dict__[attr] = val

    def get_base_update(self):
        return self._base_updates

    def get_interaction(self, others):
        return (self._interactions, None)

    def get_name(self):
        return self._name

    def get_id(self):
        self.id = generate_uuid()
        
