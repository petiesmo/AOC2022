#AOC22D8.py
from copy import deepcopy
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path 
from pprint import pprint
import math as m

def get_data():
    fi = Path(__file__)
    inp = fi.parent / f"{fi.stem}.inp"
    data = inp.read_text()
    return data.splitlines()

@dataclass
class Forest():
    trees: list[list[str]]

    def tree(self, irow, icol):
        return self.trees[irow][icol]
    
    def row(self, row_index):
        return self.trees[row_index]
    
    def col(self, col_index):
        return [row[col_index] for row in self.trees]

    def apply_to_all(self, function):
        ftree = deepcopy(self.trees)
        for irow,row in enumerate(self.trees):
            for icol,val in enumerate(row):
                ftree[irow][icol] = function(int(val))
        return ftree

    def viz(self, irow, icol):
        tree = int(self.tree(irow,icol))
        row = [int(i) for i in self.row(irow)]
        col = [int(i) for i in self.col(icol)]
        West,East = row[:icol], row[icol+1:]
        North,South = col[:irow], col[irow+1:]
        #print(f'{irow},{icol}: {North=},{South=},{East=},{West=}')
        Odirs = [-1 if len(Od)==0 else max(Od) for Od in [North,South,East,West]]
        return any([tree > Od for Od in Odirs])

    def viz_map(self):
        ftree = deepcopy(self.trees)
        for irow,row in enumerate(self.trees):
            for icol,val in enumerate(row):
                ftree[irow][icol] = self.viz(irow, icol)
        viz_trees = sum([sum(row) for row in ftree])
        print(f'{viz_trees=}')
        return ftree, viz_trees

    @staticmethod
    def trees_in_sightline(treehouse, line):
        if len(line) == 0: return 0
        count = 0
        for tree in line:
            count += 1
            if tree >= treehouse: break
        return count

    def scenic_scores(self, irow, icol):
        tree = int(self.tree(irow,icol))
        row = [int(i) for i in self.row(irow)]
        col = [int(i) for i in self.col(icol)]
        West,East = row[:icol], row[icol+1:]
        North,South = col[:irow], col[irow+1:]
        Odirs = [self.trees_in_sightline(tree, Od) for Od in [North[::-1],South,East,West[::-1]]]
        return m.prod(Odirs)

    def scenic_map(self):
        ftree = deepcopy(self.trees)
        for irow,row in enumerate(self.trees):
            for icol,val in enumerate(row):
                ftree[irow][icol] = self.scenic_scores(irow, icol)
        most_scenic = max([max(row) for row in ftree])
        print(f'{most_scenic=}')
        return ftree, most_scenic

#Part A Question:
#How many trees are visible from outside the grid?

def mainA():
    forest_data = get_data()
    forest = Forest([list(row) for row in forest_data])
    #pprint(forest.trees)
    #f2 = lambda n: 10*n
    #print(forest.apply_to_all(f2))
    viz, nviz = forest.viz_map()
    #pprint(viz)
    pprint(f'Answer A: {nviz} Trees Visible')

#Part B Question
#What is the highest scenic score possible for any tree?

def mainB():
    forest_data = get_data()
    forest = Forest([list(row) for row in forest_data])
    ss, mosts = forest.scenic_map()
    #pprint(ss)
    print(f'Answer B: Best Scenic Score: {mosts}')

if __name__ == '__main__':
    mainA()
    mainB()

#Result:
#Answer A: total_viz= 1798
#Answer B: best_score = 259308