#!/usr/bin/python3
"""
Holds the base class for a Display.

The base class can be instantiated in simulation_conf as a Console Display.
"""


class Display():
    def __init__(self):
        pass

    def render(self, persons, action_log):
        for actor, action, target in action_log:
            print('%s performed %s on %s' % (actor.get_name(), action.get_name(), target.get_name()))
        print('World State')
        for person in persons:
            print(str(person))
        print('')
