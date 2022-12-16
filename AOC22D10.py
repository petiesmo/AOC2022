#AOC22D10.py
from pprint import pprint
from pathlib import Path 
import string

def get_data():
    fi = Path(__file__)
    inp = fi.parent / f"{fi.stem}.inp"
    data = inp.read_text()
    return data.splitlines()

def read_cmd(line):
    if line == 'noop': return (1,0)
    _,v = line.split(" ")
    return (2,int(v))

def screen(wide, high):
    row = 40*'.'
    return [row for i in range(6)]

def coord(n):
    return n//40, n%40

#Part A Question:
#What is the sum of the six signal strengths of interest?

def mainA():
    instructions = get_data()
    cmds = [read_cmd(cmd) for cmd in instructions]
    Xreg = [1]
    Xnow = 1
    cycle = 0
    for ic,iv in cmds:
        for i in range(ic):
            Xreg.append(Xnow)
        Xnow += iv

    num_cycles = len(Xreg)
    cycles_of_interest = range(20,221,40)
    signal_strengths = [i*Xreg[i] for i in cycles_of_interest]
    print(f'{signal_strengths}')
    print(f'Answer A: Sum of 6 signal strengths: {sum(signal_strengths)}')
    return Xreg

#Part B Question
# Screen 40w x 6h
#Render the image given by your program. What eight capital letters appear on your CRT?

def mainB(xReg):
    print(xReg)
    scr = ['#' if cycle%40 - X in [-1,0,1] else '.' for cycle, X in enumerate(xReg[1:])]
    screen = [scr[i:i+40] for i in range(0,240,40)]
    [print(''.join(row)) for row in screen] 
    print(f'Answer B: {screen=}')

if __name__ == '__main__':
    xReg = mainA()
    mainB(xReg)

#Result:
#Answer A: Sum of 6 signal strengths: 13520
#Answer B: Display: PGPHBEAB