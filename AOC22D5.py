#AOC22D5.py
#Crate stacking

from pathlib import Path
from copy import deepcopy
import re

def get_data():
    fi = Path(__file__)
    inp = fi.parent / f"{fi.stem}.inp"
    data = inp.read_text()
    return data.splitlines()

test_stacks = [[],
    ['Z','N'],
    ['M','C','D'],
    ['P']]

stacks = [
    [],
    ['R','G','J','B','T','V','Z'],
    ['J','R','V','L'],
    ['S','Q','F'],
    ['Z','H','N','L','F','V','Q','G'],
    ['R','Q','T','J','C','S','M','W'],
    ['S','W','T','C','H','F'],
    ['D','Z','C','V','F','N','J'],
    ['L','G','Z','D','W','R','F','Q'],
    ['J','B','W','V','P']
]
shipA = deepcopy(stacks)
shipB = deepcopy(stacks)

def parse_move(move):
    result = re.search('move (\d+) from (\d+) to (\d+)', move)
    return tuple(int(r) for r in result.groups())

def move_boxes_9000(move:tuple):
    qty,frm,to = move
    for _ in range(qty):
        shipA[to].append(shipA[frm].pop(-1))
    #print(f'{ship=}')

#Part A Question:
#After the rearrangement procedure completes, what crate ends up on top of each stack?

def mainA():
    #print(f'{ship=}')
    move_data = get_data()
    moves = [parse_move(mv) for mv in move_data]
    for move in moves: move_boxes_9000(move)
    msg = ''.join([stk[-1] for stk in shipA[1:]])
    print(f'Answer A: {msg=}')

#Part B Question
#CrateMover9001 - the ability to pick up and move multiple crates at once
#After the rearrangement procedure completes, what crate ends up on top of each stack?
def move_boxes_9001(move:tuple):
    qty,frm,to = move
    shipB[to].extend(shipB[frm][-qty:])
    shipB[frm] = shipB[frm][:-qty]
    #print(f'{shipB=}')

def mainB():
    #print(f'{shipB=}')
    move_data = get_data()
    moves = [parse_move(mv) for mv in move_data]
    for move in moves: move_boxes_9001(move)
    print(shipB)
    msg = ''.join([stk[-1] for stk in shipB[1:]])
    print(f'Answer B: {msg=}')

if __name__ == '__main__':
    mainA()
    mainB()

#Result:
#Answer A: total_score= ZSQVCCJLL
#Answer B: total_score2 = QZFJRWHGS

#Result:
#Answer A: total_score= ZSQVCCJLL
#Answer B: total_score2 = QZFJRWHGS