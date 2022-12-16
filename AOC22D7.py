#AOC22D7.py

from pathlib import Path 
from pprint import pprint
import string
from dataclasses import dataclass, field

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

@dataclass
class File():
	name: str
	size: int

@dataclass
class Directory():
	name: str
	parent: None	#Directory
	capacity: int = 0
	files: list[File] = field(default_factory=list)
	dirs: dict = field(default_factory=dict)

	@property
	def size(self):
		fsize = sum([f.size for f in self.files])
		dsize = sum([d.size for k,d in self.dirs.items()])
		return fsize + dsize	

	@property
	def free_space(self):
		n = self.capacity - self.size
		return n if n>0 else 0

	def add_dir(self, name):
		self.dirs[name] = Directory(name, parent = self)
		return self.dirs[name]

	def get_dir(self, name):
		return self.dirs[name]

	def get_path(self, path:list):		
		name = path.pop(0)
		if len(path) == 0: return self.dirs[name]
		self.get_path(path)

	def show_tree(self, level:int=0, files=True, dirs=True):
		if files: pprint([f'{(level+1)*4*" "}{f.name} - {f.size}' for f in self.files])
		if dirs: pprint(f'{level*4*" "}- {self.name} (dir) - {self.size}')
		for k,d in self.dirs.items():
			d.show_tree(level+1, files, dirs)

	def filter_tree(self, min=0, max=100, level:int=0):
		if min <= self.size <= max:
			pprint(f'{level*4*" "}- {self.name} (dir) - {self.size}')
		for k,d in self.dirs.items():
			d.filter_tree(min=min, max=max, level=level+1)

	def filter_dirs(self, min=0, max=100):
		the_list = list()
		if min <= self.size <= max:
			the_list.append((self.name, self.size))
		for k,d in self.dirs.items():
			the_list.extend(d.filter_dirs(min=min, max=max))
		return the_list

#Part A Question:
# What is the sum of directory sizes of at most 100k

def mainA():
	term = get_data()
	parent = None
	drive = Directory('root', parent=None, capacity=70000000)
	drive.add_dir('/')
	cur_dir = drive
    
	iline = 0
	while iline < len(term):
		line = term[iline]
		if line is None: break
		cmd = line.split(' ')
		if cmd[1] == 'cd':
			if cmd[2] == '..':
				cur_dir = cur_dir.parent
			else:
				cur_dir = cur_dir.get_dir(cmd[2])
			iline += 1
		elif cmd[1] == 'ls':
			while True:
				iline += 1
				if iline == len(term): break
				item = term[iline]
				if item is None or is_cmd(item): break
				if is_file(item):
					fsize, fname = item.split(' ')
					cur_dir.files.append(File(fname, int(fsize)))
				if is_dir(item):
					_, dname = item.split(' ')
					cur_dir.add_dir(dname)
	

	drive.show_tree(files=False)
	print("------------------------")
	drive.filter_tree(max=100000)
	print("------------------------")
	filtered = drive.filter_dirs(max=100000)
	pprint(filtered)
	dirsum = sum([ds for dn,ds in filtered])
	print(f'Answer A: {dirsum}')

	return drive

#Part B Question
# Total Disk space is 70000000;  Free space required: 30000000
# Which folder should be deleted to acheive free space?

def mainB(disk:Directory):
	print(f'{disk.size=}')
	print(f'{disk.free_space=}')
	needed = 30000000 - disk.free_space
	filtered = disk.filter_dirs(min=needed, max=disk.size)
	print(f'{filtered=}')
	best = min([ds for dn,ds in filtered])
	print(f'Answer B: {best=}')

if __name__ == '__main__':
    drive = mainA()
    mainB(drive)

#Result:
#Answer A: total = 1648397
#Answer B: best = 1815525 ('nbq')