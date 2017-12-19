'''
Objective

Following a flood, the bank needs to be evacuated. The building of modern design
is rectangular and made of blocks. Each block has multiple levels that are
linked by a stairway. Your office is located at the top left corner of the
building and the exit is located at the bottom right corner. You can go through
a block if and only if it is higher or equal that the water level. The water
level is constant in the building. The goal of this challenge is to determine if
you can exit the building.

Data format

Input
Row 1 : 3 integers W,L and H space separated representing the width and length
of the building, and the height that the water has reached. W and L are between
2 and 50. H is between 1 and 100,000.
Row 2 to W + 1 : L integers between 1 and 100,000 separated by a space
representing the height of the block for a given row. The first value of row 2
is consequently the top left corner of the building and the last value of row
W+1 is the bottom right corner of the building.

You can only move horizontally or vertically between two points of the map.
Furthermore, top-left and bottom-right corners are at height 100,000, thus the
entrance and exit are never underwater.

Output
The string YES if you can go from your office to the exit by only going through
blocks that are higher or equal than the water level. Otherwise, the string NO.
'''
def solution(lines):
    # dfs iterative
    inputs = iter(lines)
    rows, cols, height = map(int, next(inputs).split())
    matrix = []
    for _ in range(rows):
        line = [int(i) for i in next(inputs).split()]
        matrix.append(line)
    def dfs():
        stack = [(0,0)]
        visited = set()
        while stack:
            r,c = stack.pop()
            if r==rows-1 and c==cols-1:
                return True
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr = r + dr
                nc = c + dc
                if (0<=nr<=rows-1 and 0<=nc<=cols-1 and (nr,nc) not in visited
                        and matrix[nr][nc] >= height):
                    stack.append((nr,nc))
                    visited.add((nr,nc))
        return False
    if dfs():
        print('YES')
    else:
        print('NO')

# Sample Test
import os, IsoContestTest
q = 6
test_data_path = "{0}{1}{2}".format(os.path.abspath(os.path.dirname(os.path.realpath(__file__))), os.sep, q)
IsoContestTest.print_test_result(test_data_path, solution)
