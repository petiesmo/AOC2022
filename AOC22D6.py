#AOC22D6.py

from pathlib import Path 
import string

def get_data():
    fi = Path(__file__)
    inp = fi.parent / f"{fi.stem}.inp"
    data = inp.read_text()
    return data #.splitlines()

def repeats(seq):
    return True if len(set(seq)) < len(seq) else False

def find_marker(stream, marker_length=4):
    ml = marker_length
    for i,_ in enumerate(stream[ml:], start=ml):
        window = stream[i-ml:i]
        if not repeats(window): return i, window
    print('No Marker Found...')
    return None 


#Part A Question:
#How many characters need to be processed before the first start-of-packet marker (4 non-repeating chars) is detected?

def mainA():
    stream = get_data()
    pos, marker = find_marker(stream)
    print(f'Answer A: Marker {marker} found at position {pos}')

#Part B Question
##How many characters need to be processed before the first start-of-message marker (14 non-repeating chars) is detected?

def mainB():
    stream = get_data()
    pos, marker = find_marker(stream, 14)
    print(f'Answer B: Marker {marker} found at position {pos}')

if __name__ == '__main__':
    mainA()
    mainB()

#Result:
#Answer A: total_score= 1909
#Answer B: total_score2 = 3380