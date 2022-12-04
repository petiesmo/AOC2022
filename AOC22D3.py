#AOC22D3.py

from pathlib import Path 
import string

def get_data():
    fi = Path(__file__)
    inp = fi.parent / f"{fi.stem}.inp"
    data = inp.read_text()
    return data.splitlines()

def rucksack(contents):
    li = len(contents) // 2
    l1, l2 = contents[:li], contents[li:]
    common_item = list(set(l1).intersection(set(l2)))
    if len(common_item) != 1: raise ValueError(f'Error: {contents} yielded {common_item}')
    return priority(common_item[0])

def rucksack_group(contents):
    sacks = [set(sack) for sack in contents]
    common1 = sacks[0].intersection(sacks[1])
    common2 = common1.intersection(sacks[2])
    if len(common2) != 1: raise ValueError(f'Error: {contents} yielded {common2}')
    common_item = list(common2)
    return priority(common_item[0]) 

def priority(item):
    return 1 + string.ascii_letters.index(item)

#Part A Question:
#Lowercase item types a through z have priorities 1 through 26.
#Uppercase item types A through Z have priorities 27 through 52.
#Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

def mainA():
    rucksacks = get_data()
    total_score = sum([rucksack(sack) for sack in rucksacks])
    print(f'Answer A: {total_score=}')

#Part B Question
#Groups taken 3 at a time
#Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
def split_up(list_a, chunk_size):
  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

def mainB():
    rucksacks = get_data()
    rucksack_groups = split_up(rucksacks, 3)
    total_score2 = sum([rucksack_group(sack_group) for sack_group in rucksack_groups])
    print(f'Answer B: {total_score2=}')

if __name__ == '__main__':
    mainA()
    mainB()

#Result:
#Answer A: total_score= 7850
#Answer B: total_score2 = 2581