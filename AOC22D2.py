#AOC22D2.py

from pathlib import Path 

def get_data():
    fi = Path(__file__)
    inp = fi.parent / f"{fi.stem}.inp"
    data = inp.read_text()
    return data.splitlines()

def battle(vs):
    they, me = vs.split(' ')
    m = translate[me]
    t = translate[they]
    o = outcomes[t][m]
    return m + o

#Part A Question:
#What would your total score be if everything goes exactly according to your strategy guide?
#battles = ['A Y', 'B X', 'C Z']
translate = {'A': 1, 'B': 2, 'C': 3,
             'X': 1, 'Y': 2, 'Z': 3}

outcomes = [
    [0, 0, 0, 0],
    [0, 3, 6, 0],
    [0, 0, 3, 6],
    [0, 6, 0, 3]
]
battles = get_data()
total_score = sum([battle(vs) for vs in battles])
print(f'Answer A: {total_score=}')

#Part B Question
#the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
#What would your total score be if everything goes exactly according to your strategy guide?
translate2 = {'A': 1, 'B': 2, 'C': 3,
              'X': 0, 'Y': 3, 'Z': 6,
               0: 1, 3: 2, 6: 3}

outcomes2 = [
    [0, 0, 0, 0],
    [0, 3, 1, 2],
    [0, 1, 2, 3],
    [0, 2, 3, 1]
]
def battle2(vs):
    they, outcome = vs.split(' ')
    t = translate2[they]
    o = translate2[outcome]
    o2 = translate2[o]
    m = outcomes2[t][o2]
    #print(t,o,o2,m)
    return m + o

#battles = ['A Y', 'B X', 'C Z']
#print([battle2(vs) for vs in battles])
total_score2 = sum([battle2(vs) for vs in battles])
print(f'Answer B: {total_score2=}')

#Result:
#Answer A: total_score= 13005
#Answer B: total_score2 = 11373