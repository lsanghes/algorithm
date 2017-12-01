'''
This challenge is based on the game of life you will find the principles here:
http://fr.wikipedia.org/wiki/Jeu_de_la_vie.

In this embodiment, at each stage - when a cell has a neighbor living above and
a lively neighbor left: it becomes alive;

- When a cell has no living close either above or to the left: it dies;
- In the remaining cases, it retains its status.

You must specify the time of survival of the population from an initial
configuration. Ie the number of steps after which it no longer living cell.

For convenience, the initial configuration will be described by a series of
rectangles of living cells.

Data format

Input
Line 1: an integer N between 1 and 1000 representing the number of rectangles.
Lines 2 to N + 1: four integers x1 y1 x2 y2 each between 1 and 1 000 000 and
    separated by spaces. All items included in the rectangle bounded by x1, y1
    (upper-left corner) and x2, y2 (bottom-right) are living cells. Indeed,
    the x are increasing to the right, and the ordinates are growing downward.

There will be no more than one million live cells at the start.

Output
An integer representing the time of survival of the population. If the
population survives indefinitely, return -1.

Example
[. . . . x .][. . . . . .][. . . . . .][. . . . . .][. . . . . .][. . . . . .]
[. x x x . .][. . x x x .][. . . x x .][. . . . x .][. . . . . .][. . . . . .]
[. x . . . .][. x x . . .][. . x x . .][. . . x x .][. . . . x .][. . . . . .]
[. X . . . .][. x . . . .][. x x . . .][. . x x . .][. . . x x .][. . . . x .]
[. . . . . .][. . . . . .][. . . . . .][. . . . . .][. . . . . .][. . . . . .]
[. . . . . .][. . . . . .][. . . . . .][. . . . . .][. . . . . .][. . . . . .]

This generation, designated on the image while the left by the following test
3 rectangles:

3
5 1 5 1
2 2 4 2
2 3 2 4

has a life of 6.
'''
# TLE - calculate life span by interation
def solution1(lines):
    cur_live = set()
    for line in lines[1:]:
        col1, row1, col2, row2 = map(lambda x: int(x)-1, line.split())
        for r in range(row1, row2+1):
            for c in range(col1, col2+1):
                cur_live.add((r,c))
    total_life_span = 1
    while cur_live:
        next_live = set()
        for r,c in cur_live:
            if (r+1, c-1) in cur_live:
                next_live.add((r+1, c))
            if (r-1, c+1) in cur_live:
                next_live.add((r, c+1))
        for r,c in cur_live:
            if (r-1, c) in cur_live or (r, c-1) in cur_live:
                next_live.add((r, c))
        cur_live = next_live
        total_life_span +=1
    print(total_life_span-1)

# serach using union find
def solution2(lines):
    inputs = iter(lines)
    N = int(next(inputs))
    uf = UnionFind(N)
    max_x = [0] * N
    max_y = [0] * N
    min_c = [0] * N
    rectangles = []
    for i in range(N):
        x1, y1, x2, y2 = map(int, next(inputs).split())
        max_x[i] = x2
        max_y[i] = y2
        min_c[i] = x1 + y1
        for j in range(i):
            x1a, y1a, x2a, y2a = rectangles[j]
            if not (x2a + 1 < x1 or x2 + 1 < x1a or y2a + 1 < y1 or y2 + 1 < y1a) and not (x2a + 1 == x1 and y2a + 1 == y1) and not (x2 + 1 == x1a and y2 + 1 == y1a):
                ii = uf.find(i)
                jj = uf.find(j)
                uf.union(i, j)
                k = uf.find(i)
                max_x[k] = max([max_x[k], max_x[ii], max_x[jj]])
                max_y[k] = max([max_y[k], max_y[ii], max_y[jj]])
                min_c[k] = min([min_c[k], min_c[ii], min_c[jj]])
        rectangles.append((x1, y1, x2, y2))
    lifespan = 0
    for i in range(N):
        k = uf.find(i)
        if max_x[k] + max_y[k] - min_c[k] + 1 > lifespan:
            lifespan = max_x[k] + max_y[k] - min_c[k] + 1
    print(lifespan)

class UnionFind:
    def __init__(self, n):
        self.pere = list(range(n))
        self.rang = [0] * n

    def find(self, x):
        if self.pere[x] == x:
            return x
        else:
            repr_x = self.find(self.pere[x])
            self.pere[x] = repr_x
            return repr_x

    def union(self, x, y):
        repr_x = self.find(x)
        repr_y = self.find(y)
        if repr_x == repr_y:
            return False
        if self.rang[repr_x] == self.rang[repr_y]:
            self.rang[repr_x] += 1
            self.pere[repr_y] = repr_x
        elif self.rang[repr_x] > self.rang[repr_y]:
            self.pere[repr_y] = repr_x
        else:
            self.pere[repr_x] = repr_y
        return True

# Sample Test
import os, IsoContestTest
file_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
data_path = file_path + os.sep  + '7'
IsoContestTest.print_test_result(data_path, solution1)
IsoContestTest.print_test_result(data_path, solution2)
