#AOC22D4.py

from pathlib import Path 
import string

def get_data():
    fi = Path(__file__)
    inp = fi.parent / f"{fi.stem}.inp"
    data = inp.read_text()
    return data.splitlines()

def ranges(pair):
    ranges = [rg.split('-') for rg in pair.split(',')]
    spans = [list(range(int(a),int(b)+1)) for a,b in ranges]
    return spans

def fully_contains(r1,r2):
    return True if all([item in r2 for item in r1]) or all([item in r1 for item in r2]) else False

def overlaps(r1,r2):
    return True if set(r1).intersection(r2) else False

#Part A Question:
#In how many assignment pairs does one range fully contain the other?

def mainA():
    pairs = get_data()
    the_ranges = [ranges(pair) for pair in pairs]
    print(the_ranges)
    engulfs = [fully_contains(r1,r2) for r1,r2 in the_ranges]
    print(engulfs)
    total_within = [p for p in engulfs if p]
    print(f'Answer A: {len(total_within)} pairs fully contain another')

#Part B Question
#In how many assignment pairs do the ranges overlap at all?


def mainB():
    pairs = get_data()
    the_ranges = [ranges(pair) for pair in pairs]
    print(the_ranges)
    touches = [overlaps(r1,r2) for r1,r2 in the_ranges]
    print(touches)
    total_touch = [p for p in touches if p]
    print(f'Answer B: {len(total_touch)} pairs partially overlap')

if __name__ == '__main__':
    mainA()
    mainB()

#Result:
#Answer A: total_score= 498
#Answer B: total_score2 = 859