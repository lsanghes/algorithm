'''
Given N * M field of O's and X's, where O=white, X=black
Return the number of black shapes. A black shape consists of one or more
adjacent X's (diagonals not included)

Example:

OOOXOOO
OOXXOXO
OXOOOXO

answer is 3 shapes are  :
(i)    X
     X X
(ii)
      X
 (iii)
      X
      X
Note that we are looking for connected shapes here.

For example,

XXX
XXX
XXX
is just one single connected black shape.
'''
class Solution:
    # @param A : list of strings
    # @return an integer

    # if we find one X, there is one shape.
    # use dfs to visit all connected adjacent X for the same shape.
    # if we then find another unvisited X, it must belong to a new shape!
    def black(self, A):
        def dfs(r, c): # mark all adjacent X as visited
            stack = [(r,c)]
            while stack:
                r, c = stack.pop()
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    nr, nc = r + dr, c + dc
                    if (nr, nc) not in visited \
                        and 0 <= nr < rows and 0 <= nc < cols \
                        and A[nr][nc] == 'X':
                        stack.append((nr, nc))
                        visited.add((nr, nc))
        rows = len(A)
        cols = len(A[0])
        visited = set()
        res = 0
        for r in range(rows):
            for c in range(cols):
                if A[r][c] == 'X' and (r,c) not in visited:
                    res += 1 # found a new shape
                    visited.add((r, c)) # mark this X as visited
                    dfs(r,c) # mark all adjacent X as visited
        return res

# test
print(Solution().black(['OOOXOOO',
                        'OOXXOXO',
                        'OXOOOXO']))
