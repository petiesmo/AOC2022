#AOC22D7.py

from pathlib import Path 
import string
from dataclass import dataclass, Field

def get_data():
    fi = Path(__file__)
    inp = fi.parent / f"{fi.stem}.inp"
    data = inp.read_text()
    return data.splitlines()

def is_cmd(line):
	return True if line.startswith('$ ') else False
	
def is_dir(line):
	return True if line.startswith('dir ') else False
	
def is_file(line):
	return True if line[0].isnumeric() else False

def get_dir(drive, path):
	idir = drive.copy()
	for step in path:
		idir = idir[step]
	return idir

def get_dir_size(this_dir, dir_sizes):
	size = sum([f[0] for f in idir['files']])
	dirs = [k for k in this_dir.keys() if k not in ['files','size']]
	if len(dirs) > 0:
		for idir in dirs:
			dir_sizes = get_dir_size(idir, dir_sizes) 
	dir_sizes.append(size)
	return dir_sizes
		

#Part A Question:
# What is the sum of directory size of at most 100k

def mainA():
    term = get_data()
    cur_path = []
    drive = {}
    cur_dir = drive
    
    line = next(term, None)
    while line is not None
		cmd = line.split(' ')
		if cmd[1] == 'cd':
			if cmd[2] == '..':
				cur_path.pop()
				cur_dir = get_dir(drive, cur_path)
			else:
				cur_dir = cur_dir[cmd[2]]
				cur_path.append(cmd[2])
			line = next(term)
		elif cmd == 'ls':
			item = next(term, None)
			while item is not None or not is_cmd(item):
				if is_file(item):
					cur_dir['files'].append(tuple(item.split(' ')))
				if is_dir(item):
					cur_dir[item] = {'files':[], 'size':0}
				item = next(term, None)
			line = item
		    
	dirsum = sum([ds for ds in get_dir_sizes(drive, []) if ds <= 100000])
    print(f'Answer A: {dirsum}')

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