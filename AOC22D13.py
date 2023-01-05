#AOC22D13.py
#Distress Signal
from dataclasses import dataclass
from pathlib import Path 
from pprint import pprint
import string

def get_data():
    fi = Path(__file__)
    inp = fi.parent / f"{fi.stem}.inp"
    data = inp.read_text()
    return [tuple(pair.split('\n')) for pair in data.split('\n\n')]

def packet_in_right_order(pair):
    result = True
    return result

def compare(A, B):
    A1, B1 = A.pop(0), B.pop(0)
    if type(A1) == 'int' and type(B1) == 'int':
        if B1 > A1: return False
    return compare(A, B)

#Part A Question:
# You need to identify how many pairs of packets are in the right order.
# What is the sum of the indices of those pairs that are already in the right order?

def mainA():
    pairs = get_data()
    pprint(pairs)
    print(f'Answer A: {len(pairs)} something')

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

#Comparison Criteria:
#If both values are integers, the lower integer should come first. If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
#If both values are lists, compare the first value of each list, then the second value, and so on. If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
#If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].