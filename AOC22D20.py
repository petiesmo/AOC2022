#AOC22D20.py
from dataclasses import dataclass, field
from pathlib import Path 
from pprint import pprint
import string

def get_data():
    fi = Path(__file__)
    inp = fi.parent / f"{fi.stem}.inp"
    data = inp.read_text()
    return data.splitlines()

@dataclass
class Byte():
    id: int
    value: int

@dataclass(init=False)
class Message():
    
    def __init__(self, encrypted, dkey=1):
        self.encrypted = tuple((Byte(i,int(b)*dkey) for i,b in enumerate(encrypted)))
        self.decrypted = list(self.encrypted)
        self.msg_length = len(self.encrypted)

    def decrypt(self):
        # 'Mixing' decryption: The byte moves from its current position, by an amount equal to its value
        # The list is circular, and indices will 'wrap around' 
        for byte in self.encrypted:
            if byte.value == 0: continue
            cur_index = self.decrypted.index(byte)
            new_index = (cur_index + byte.value) % (self.msg_length-1)
            self.decrypted.insert(new_index, self.decrypted.pop(cur_index))
            #print(byte, [b.value for b in self.decrypted])

    def grove_coord(self):
        msg_vals = [b.value for b in self.decrypted]
        izero = msg_vals.index(0)
        offsets = [1000,2000,3000]
        coords = [msg_vals[(izero + offset) % self.msg_length] for offset in offsets]
        print(f'{msg_vals=}')
        print(f'{coords=}')
        print(f'{sum(coords)}')
        return sum(coords)

#Part A Question:
#Mix the encrypted file exactly once.  What is the sum of the three numbers that form the grove coordinates? 

def mainA():
    tx = get_data()
    msg = Message(tx)
    msg.decrypt()
    coord_sum = msg.grove_coord()
    print(f'Answer A: {coord_sum}')

#Part B Question
#Apply the decryption key, and decrypt 10x.  Now what is the sum?

def mainB():
    dkey = 811589153
    tx = get_data()
    msg = Message(tx, dkey=dkey)
    for i in range(10):
        msg.decrypt()
        print(f'Round {i}: {[b.value for b in msg.decrypted]}')
    coord_sum = msg.grove_coord()
    print(f'Answer B: {coord_sum}')

if __name__ == '__main__':
    mainA()
    mainB()

#Result:
#Answer A: 19070
#Answer B: 14773357352059