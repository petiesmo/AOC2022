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
        self.leaf = True
        self.parse_job(job)

    @classmethod
    def set_monkey_data(cls, monkey_data):
        cls.monkeys = monkey_data
    
    def parse_job(self, job):
        if job.isnumeric(): 
            self.left, self.right, self.oper = int(job), 0, ' + '
        else: 
            self.leaf = False
            L, self.oper, R = tuple(re.match('(\w+)(\s.\s)(\w+)', job).groups())
            self.left, self.right = Monkey(L, self.monkeys[L]), Monkey(R, self.monkeys[R])
    
    def do_job(self, A, B, oper):
        #print(self.name, A, B, oper)
        if oper==' + ': return int(A+B)
        if oper==' - ': return int(A-B)
        if oper==' * ': return int(A*B)
        if oper==' / ': return int(A/B)
        return A

    @property
    def value(self):
        if self.leaf: return self.left
        return self.do_job(self.left.value, self.right.value, self.oper)


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
    monkey_data = get_data()
    print(monkey_data[-5:])
    monkeys = {k:v for k,v in monkey_data}
    Monkey.set_monkey_data(monkeys)
    # A bit "brute force" for my taste, but want to get 'er done
    monkeys['humn'] = '3640000000000'
    inc = 1000000000
    while True:
        root_left = Monkey('cmmh', monkeys['cmmh'])
        root_right = Monkey('lqcd', monkeys['lqcd'])
        print(f"Humn: {monkeys['humn']}: ({root_left.value} vs {root_right.value}) ({(root_left.value-root_right.value) / root_right.value:.5})")
        if root_left.value == root_right.value: break
        if root_left.value < root_right.value: 
            monkeys['humn'] = str(int(monkeys['humn']) - inc)
            inc = inc // 10
        monkeys['humn'] = str(int(monkeys['humn']) + inc)
    print(f"Answer B: Human needs to yell {monkeys['humn']}!")

if __name__ == '__main__':
    mainA()
    mainB()

#Result:
#Answer A: Root monkey yells 38914458159166!
#Answer B: Human needs to yell 3665520865940!