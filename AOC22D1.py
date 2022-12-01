#AOC22D1.py

from pathlib import Path 

fi = Path(__file__)
inp = fi.parent / f"{fi.stem}.inp"

data = inp.read_text()

elf = list()
elves = list()

for d in data.splitlines():
    if d.strip():
        elf.append(int(d))
    else:
        elves.append(elf)
        elf = list()

#Part A Question:
#Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
most_cal = max([sum(elf) for elf in elves])
print(f'Answer A: {most_cal=}')

#Part B Question
#Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
elf_sort = sorted([sum(elf) for elf in elves], reverse=True)
top_three = sum(elf_sort[:3])
print(f'Answer B: {top_three=}')

#Result:
#Answer A: most_cal=71471
#Answer B: top_three=211189