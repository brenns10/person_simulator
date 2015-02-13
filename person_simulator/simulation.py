#!/usr/bin/python3
"""
Control script for person_simulator. 

Will have the option to run in a tmux instance or in the console.
"""
from argparse import ArgumentParser
from subprocess import Popen, PIPE
from world import World
from time import sleep
from simulation_conf import CONF as config


def load_persons():
    return {p.get_id(): p for p in config.get('persons', [])}


def load_displays():
    # TODO: load displays from `/displays` directory
    return config.get('displays', [])


def start_simulation():
    world = World(load_persons(), load_displays())
    while True:
        print('simulation: tick')
        world.on_tick()
        sleep(5)


if __name__ == '__main__':
    p = ArgumentParser('A script for managing person_simulator.')
    p.add_argument('-d', '--daemon', action='store_true', help='Launches person_simulator in tmux as a daemon.')
    args = p.parse_args()

    if args.daemon:
        # TODO: call out to tmux to start daemon
        print('Daemon mode not yet supported.')
    else:
        try:
            start_simulation()
        except KeyboardInterrupt:
            print('Exiting person_simulator...')
            exit(0)
            
