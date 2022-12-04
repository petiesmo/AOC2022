#AOC22D5.py

from pathlib import Path 
import string

def get_data():
    fi = Path(__file__)
    inp = fi.parent / f"{fi.stem}.inp"
    data = inp.read_text()
    return data.splitlines()

def ranges(pair):
    pass

#Part A Question:
#In how many assignment pairs does one range fully contain the other?

def mainA():
    pairs = get_data()
    print(f'Answer A: {len([1])}something')

#Part B Question
#In how many assignment pairs do the ranges overlap at all?

def mainB():
    pairs = get_data()
    print(f'Answer B: {len([1])} something')

if __name__ == '__main__':
    mainA()
    #mainB()

#Result:
#Answer A: total_score= 498
#Answer B: total_score2 = 2581