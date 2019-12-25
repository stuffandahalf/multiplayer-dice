#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# compatibility imports
from builtins import input

import random

def USER_PROMPT(user_id): return 'Set the name of player {}: '.format(user_id)
def ROLL_PROMPT(): return 'Roll? '
def ROLL_RESPONSE(user, roll): return '{} rolls {}'.format(user, roll)

def main(args):
    max_dice = 6
    players = []
    
    if len(args) == 2:
        max_dice = int(args[1])
    
    line = input(USER_PROMPT(len(players) + 1))
    while line != '':
        players.append(line)
        line = input(USER_PROMPT(len(players) + 1))
    
    if len(players) == 0:
        print('You must have at least one player to roll the dice')
        return 1
    
    index = 0
    roll = random.randint(1, max_dice)
    line = input(ROLL_PROMPT())
    while line.upper() != 'N':
        print(ROLL_RESPONSE(players[index], roll))
        index = (index + 1) % len(players)
        roll = random.randint(1, max_dice)
        line = input(ROLL_PROMPT())
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
