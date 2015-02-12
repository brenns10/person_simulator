#!/usr/bin/python3
"""
Control script for person_simulator. 

Will have the option to run in a tmux instance or in the console.
"""
from argparse import ArgumentParser
from subprocess import Popen, PIPE
from world import World
from time import sleep


def start_simulation():
    world = World()
    while True:
        print('simulation: tick')
        world.on_tick()
        sleep(5)


if __name__ == '__main__':
    p = ArgumentParser('A script for managing person_simulator.')
    p.add_argument('-d', '--daemon', help='Launches person_simulator in tmux as a daemon.')
    args = p.parse_args()

    if args.daemon:
        # TODO: call out to tmux to start daemon
        print('Daemon mode not yet supported')
    else:
        try:
            start_simulation()
        except KeyboardInterrupt:
            print('Exiting person_simulator...')
            exit(0)
            
