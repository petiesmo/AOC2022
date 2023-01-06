#AOC22D13.py
#Distress Signal
from dataclasses import dataclass
import math
from pathlib import Path 
from pprint import pprint
from itertools import zip_longest

def get_data():
    fi = Path(__file__)
    inp = fi.parent / f"{fi.stem}.inp"
    data = inp.read_text()
    return data

def new_list(packet):
    ''' Read packet left to right, drilling recursively into lists as nested elements'''
    packet = list(packet)
    the_list = list()
    buffer = ''
    while True:
        if len(packet) == 0: return buffer, ''
        ch = packet.pop(0)
        if ch == '[': 
            buffer, packet = new_list(packet)
        elif ch in ',]':
            if type(buffer) == str and buffer.isnumeric(): buffer = int(buffer)
            the_list.append(buffer)
            buffer = ''
            if ch == ']':
                return the_list, packet
        else:
            buffer += ch
    return None

def compare(A, B):
    ''' Comparison Rule set as given in AOC problem statement:
        - If both values are integers, the lower integer should come first. If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
        - If both values are lists, compare the first value of each list, then the second value, and so on. If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
        - If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].
        Note: comparison is triggered when first True or False value is identified (i.e., ignore remainder of list)
    '''
    if not type(A) == type(B):
        if type(A) == int: A = [A]
        if type(B) == int: B = [B]
    if A is None: return True
    if B is None: return False
    if type(A) == type(B) == int:
        if A > B: return False
        if A < B: return True
        return None
    else:
        test = list(zip(A,B))
        for x,y in zip_longest(A,B):
            c = compare(x,y)
            if c is not None: return c

#Part A Question:
# You need to identify how many pairs of packets are in the right order.
# What is the sum of the indices of those pairs that are already in the right order?

def mainA():
    data = get_data()
    pairs = [tuple(pair.split('\n')) for pair in data.split('\n\n')]
    parsed_pairs = list()
    for A,B in pairs:
        lA,_ = new_list(A)
        lB,_ = new_list(B)
        parsed_pairs.append((lA,lB))
    pprint(parsed_pairs)
    res = [compare(A,B) for A,B in parsed_pairs]
    pprint(res)
    answer = sum([i+1 if B else 0 for i,B in enumerate(res)])
    print(f'Answer A: Sum is {answer}')

#Part B Question
#Including 2 divider packets [[2]], [[6]], reorder all packets to be in the right order
#Find decoder key, which is the product of the 2 indices of the divider packets

def mainB():
    data = get_data()
    data = data.replace('\n\n', '\n')
    packets = list()
    for packet in data.splitlines():
        lA,_ = new_list(packet)
        packets.append(lA)
    dividers = [[[2]], [[6]]]
    packets.extend(dividers)
    sorted_packets = list()
    sorted_packets.append(packets[0])
    #Compare packets to one another sequentially
    for packet in packets[1:]:
        for i,sp in enumerate(sorted_packets):
            if compare(packet, sp):
                sorted_packets.insert(i, packet)
                break
        else:
            sorted_packets.append(packet)

    decoder_key = math.prod([sorted_packets.index(divider)+1 for divider in dividers])
    print(f'Answer B: {decoder_key=}')

def testC():
    seq = '[1,[2,[3,[4,[5,6,7]]]],8,9]'
    res,_ = new_list(seq)
    pprint(res)

if __name__ == '__main__':
    mainA()
    mainB()
    #testC()

#Result:
#Answer A: Sum is 5675
#Answer B: Decoder key is 20383