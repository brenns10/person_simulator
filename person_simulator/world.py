"""
Contains the World class, the container for most of the simulation's data.
"""
from random import shuffle
from importlib import import_module
import os
import re

class World():
    def __init__(self, persons, displays):
        self._persons = persons
        self._displays = displays
        
    def on_tick(self):
        action_log = []
        self._update(action_log)
        self._render(self._displays, action_log)

    def _update(self, action_log):
        persons = self._get_persons_list()
        shuffle(persons)
        # First: base updates
        for person in persons:
            actions = person.get_base_update()
            for action in actions:
                self._do(person, action, person, action_log)
        # Second: interactions
        # NOTE: interaction polling process subject to change
        for person in persons:
            others = set(persons) - set([person])
            action, target = person.get_interaction(others)
            if target is None:
                targets = others
            else:
                targets = [target]
            for target in targets:
                self._do(person, action, target, action_log)


    def _render(self, displays, action_log):
        for display in displays:
            display.render(self._get_persons_list(), action_log)

    def _load_modules_from_dir(self, dir_name):
        """Returns a list of all modules in the specified directory."""
        PYTHON_MODULE_PATT = r'(?P<mod_name>[^_].*)\.py'
        files = os.listdir(dir_name)
        modules = []
        for f in files:
            m = re.match(PYTHON_MODULE_PATT, f)
            if m is not None:
                mod_name = m.group('mod_name')
                modules.append(import_module('%s.%s' % (dir_name, mod_name)))
        return modules
        
    def _get_persons_list(self):
        """Returns a new list of all the people in the world."""
        return [p for p in self._persons.values()]

    def _do(self, actor, action, target, action_log):
        """Performs `actor` taking `action` on `target`, does book-keeping"""
        action_log.append((actor, action, target))
        target = action(actor, target)
