"""
Contains the World class, the container for most of the simulation's data.
"""

from random import shuffle


class World():
    def __init__(self):
        self._persons = self._load_persons()
        self._displays = self._load_displays()
        
    def on_tick(self, displays):
        action_log = []
        self._update(action_log)
        self._render(self.displays, action_log)

    def _update(self, action_log):
        persons = self._get_persons_list()
        random.shuffle(persons)
        # First: base updates
        for person in persons:
            actions = person.get_base_update()
            for action in actions:
                self._do(person, action, person, action_log)
        # Second: interactions
        # NOTE: interaction polling process subject to change
        for person in persons:
            others = set(persons) - person
            action, target = person.get_interaction(others)
            if target is None:
                targets = others
            else:
                targets = [target]
            for target in targets:
                self._do(person, action, target, action_log)

    def _render(self, displays, action_log):
        for display in displays:
            display.render(self, action_log)

    def _load_persons(self):
        # TODO: load persons from the `/persons` directory
        persons = {}
        return persons

    def _load_displays(self):
        # TODO: load displays from `/displays` directory
        displays = []
        return displays

    def _get_persons_list(self):
        """Returns a new list of all the people in the world."""
        return self._persons.values()[:]

    def _do(self, actor, action, target, action_log):
        """Performs `actor` taking `action` on `target`, does book-keeping"""
        action_log.append((actor, action, target))
        target = action(actor, target)
