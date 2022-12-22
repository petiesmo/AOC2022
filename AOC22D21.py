#AOC22D21.py
from dataclasses import dataclass
from pathlib import Path 
from pprint import pprint
import re

def get_data():
    fi = Path(__file__)
    inp = fi.parent / f"{fi.stem}.inp"
    data = inp.read_text()
    return [monkey.split(': ') for monkey in data.splitlines()]

class Monkey():
    monkeys = dict()

    def __init__(self, name:str, job:str):
        self.name = name
        self.leaf = False
        self.job = self.parse_job(job)
        self.children = self.parse_children(self.monkeys)
        self.value = self.do_job(*self.job)

    @classmethod
    def set_monkey_data(cls, monkey_data):
        cls.monkeys = monkey_data
    
    def parse_job(self, job):
        if job.isnumeric(): 
            self.leaf = True
            return (int(job), ' + ', 0)
        return tuple(re.match('(\w+)(\s.\s)(\w+)', job).groups())

    def parse_children(self, monkeys):
        if self.leaf: return None
        kid_names = (self.job[0], self.job[2])
        kids = [Monkey(kn, monkeys[kn]) for kn in kid_names]
        self.job = (kids[0].value, self.job[1], kids[1].value)
        return tuple(kids)
    
    def do_job(self, A, oper, B):
        if oper==' + ': return int(A+B)
        if oper==' - ': return int(A-B)
        if oper==' * ': return int(A*B)
        if oper==' / ': return int(A/B)
        return A

    #@property
    #def value(self):
    #    self.do_job(*self.job)

#Part A Question:
#What number will the monkey named root yell?

def mainA():
    monkey_data = get_data()
    print(monkey_data[:5])
    monkeys = {k:v for k,v in monkey_data}
    Monkey.set_monkey_data(monkeys)
    root = Monkey('root', monkeys['root'])
    print(f'Answer A: Root monkey yells {root.value}!')

#Part B Question
#Root's operation is now EQUALITY; Set HUMN value to make equality
#What number do you yell to pass root's equality test?

def mainB():
    pairs = get_data()
    print(f'Answer B: {len([1])} something')

if __name__ == '__main__':
    mainA()
    #mainB()

#Result:
#Answer A: Root monkey yells 38914458159166!
#Answer B: total_score2 = 2581