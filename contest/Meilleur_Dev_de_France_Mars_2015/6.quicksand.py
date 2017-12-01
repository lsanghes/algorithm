'''
The aim of this challenge is to determine the greatest depth of a quicksand
area in a desert. The desert is a rectangle made of points that are either
solid ground or quicksand. The depth of a quicksand point is the minimum
number of horizontal and/or vertical moves that are needed to reach a solid
ground point.
                    . . . . . . . .
                    . . 1 1 1 1 1 .
                    . 1(2)2 2 2 1 .
                    . 1 1 1 1 1 1 .
                    . . . . . . . .

In the above example, solid ground points are represented by . and the digits
represent the depth of the quicksand area. The red point has a depth equal to
2 because at least two horizontal and/or vertical moves are required to reach
a solid ground point (for example one move up and one move left or two left
moves).

Solid ground is not necessarily continuous, there may be “islands” in the
middle of quicksands. Also, there is only solid ground all along the hedges
of the map.

Data Format

Input
Row 1: two integers W and H comprised between 3 and 40 separated by a space,
    representing the width and height of the map.
Rows 2 to H+1: the rows of the map represented by strings of W characters.
    Strings are made of . characters (solid ground) or # (quicksand).

Output
An integer representing the highest depth of the quicksand areas on the map.
'''
### bfs
def solution1(lines):
    from collections import deque
    rows, cols = map(int, lines[0].split())
    grid = lines[1:]
    max_depth = 0
    queue = deque()
    visited = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.':
                queue.append((r,c,0))
                visited.add((r,c))
    while queue:
        for _ in range(len(queue)):
            r, c, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                     queue.append((nr, nc, depth+1))
                     visited.add((nr, nc))
    print(max_depth)

### forward/backward
def solution2(lines):
    rows, cols = map(int, lines[0].split())
    grid = []
    for line in lines[1:]:
        grid.append(list(line))
    ds = [[0] * cols for _ in range(rows)]  # distance for each point
    for r in range(1, rows-1):              # left and top
        for c in range(1, cols-1):
            ds[r][c] = ds[r][c-1] + 1 if grid[r][c] == '#' else 0
            ds[r][c] = min(ds[r-1][c] + 1, ds[r][c])
    for r in reversed(range(1, rows-1)):    # right and bottom
        for c in reversed(range(1, cols-1)):
            ds[r][c] = min(ds[r][c+1] + 1, ds[r][c])
            ds[r][c] = min(ds[r+1][c] + 1, ds[r][c])
    print(max([d for row in ds for d in row]))

# Sample Test
import os, IsoContestTest
file_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
data_path = file_path + os.sep  + '6'
IsoContestTest.print_test_result(data_path, solution1)
IsoContestTest.print_test_result(data_path, solution2)
