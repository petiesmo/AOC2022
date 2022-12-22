#AOC22D5.py

from dataclasses import dataclass
from pathlib import Path 
from pprint import pprint
from functools import reduce

def get_data():
    fi = Path(__file__)
    inp = fi.parent / f"{fi.stem}.inp"
    data = inp.read_text()
    data = data.split('\n\n')
    return [d.splitlines() for d in data]

@dataclass
class Item():
    num: int
    score: int

@dataclass()
class Monkey():
    num:str
    items:str
    oper:str
    test:str
    Tout:str
    Fout:str

    def __post_init__(self):
        self.num = int(self.num.split(' ')[1].replace(':',''))
        self.items = [int(i) for i in self.items.split(': ')[1].split(', ')]
        self.op = self.oper.split(' = ')[1]
        self.test = int(self.test.split(' ')[-1])
        self.Tout = int(self.Tout.split(' ')[-1])
        self.Fout = int(self.Fout.split(' ')[-1])
        self.inspect_count = 0

    def operation(self, old):
        return eval(self.op)
    
    def test_div_by(self, num):
        return num % self.test == 0

    def throw(self):
        return self.items.pop(0)

    def catch(self, thing):
        self.items.append(thing)

    def examine_item_and_throw(self, item, relief=True):
        worry = self.operation(int(item))
        worry = worry // 3 if relief else worry
        return (worry, self.Tout) if self.test_div_by(worry) else (worry, self.Fout)

    def take_turn(self, relief=True):
        actions = [self.examine_item_and_throw(item, relief) for item in self.items]
        self.inspect_count += len(self.items)
        self.items = []
        return actions

def gcd(a,b):
    if b == 0: return a
    return gcd(b, a%b)

def lcm(a,b):
    return (a*b) // gcd(a,b)

def find_lcm(items:list):
    return reduce(lcm,items)

@dataclass
class Monkey_House():              
    monkeys:list
    Round: int = 0

    def __post_init__(self):
        # Least common multiple of the Test values  (Chinese remainder theorem - thanks Reddit)
        self.LCM = find_lcm([m.test for m in self.monkeys])
        
    def process_actions(self, actions):
        for item_worry, monkey_num in actions:
            self.monkeys[monkey_num].catch(item_worry)

    def do_a_round(self, relief=True):
        for monkey in self.monkeys:
            actions = monkey.take_turn(relief)
            self.process_actions(actions)
        if not relief:
            self.manually_relieve_worry()
        self.Round += 1

    def manually_relieve_worry(self):
        f = lambda n: n % self.LCM        
        for monkey in self.monkeys:
            monkey.items = list(map(f, monkey.items))
        
    def monkey_business(self):
        mkey = [m.inspect_count for m in self.monkeys]
        msort = sorted(mkey, reverse=True)
        return msort[0] * msort[1]

    def print_monkeys(self):
        print(f'After Round {self.Round}:')
        pprint([f'Monkey {m.num}: {m.inspect_count} - {m.items}' for m in self.monkeys])
        pprint(f'Monkey Business: {self.monkey_business()}')
        pprint('---------------------------')


#Part A Question:
#What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?

def mainA():
    mdata = get_data()
    mhouse = Monkey_House([Monkey(*tuple(m)) for m in mdata])
    
    mhouse.print_monkeys()
    for _ in range(20):    
        mhouse.do_a_round()
    mhouse.print_monkeys()

    print(f'Answer A: 20 Round Monkey Business: {mhouse.monkey_business()}')

#Part B Question
# If the Relief no longer divides your worry by 3, (*You have to find a different way to reduce worry)
# what is the level of monkey business after 10000 rounds?

def mainB():
    mdata = get_data()
    mhouse = Monkey_House([Monkey(*tuple(m)) for m in mdata])
    
    mhouse.print_monkeys()
    for i in range(10000):    
        mhouse.do_a_round(relief=False)
        if i%1000 == 0: mhouse.print_monkeys()
    mhouse.print_monkeys()

    print(f'Answer B: 10k Round Monkey Business: {mhouse.monkey_business()}')

if __name__ == '__main__':
    mainA()
    mainB()

#Result:
#Answer A: 20 Round Monkey Business: 88208
#Answer B: 10k Round Monkey Business: 21115867968