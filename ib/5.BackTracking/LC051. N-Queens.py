'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space
respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
   [".Q..",  // Solution 1
    "...Q",
    "Q...",
    "..Q."],

   ["..Q.",  // Solution 2
    "Q...",
    "...Q",
    ".Q.."]
]
'''
# 4 x 4
# . Q . .
# . . . Q
# Q . . .
# . . Q .
class Solution:
    # dfs resursive
    # y = row and x = col, queens contains list of x position for each row
    # how to identify diagnoal: x1+y1 = x2+y2 or x1-y1 = x2-y2
    def solveNQueens(self, n):
        def dfs(queens, xy_sum, xy_diff):
            y = len(queens) # next row we need to work on
            if y == n:
                res.append(queens)
                return
            for x in range(n): # each row has n choices
                if x not in queens and y+x not in xy_sum and x-y not in xy_diff:
                    dfs(queens+[x], xy_sum+[y+x], xy_diff+[x-y])
        res = []
        dfs([], [], [])
        return [['.' * i + 'Q' + '.' * (n-i-1) for i in xs] for xs in res]

    # dfs iterative
    def solveNQueens2(self, n):
        res = []
        stack = [([], [], [])]
        while stack:
            queens, xy_sum, xy_diff = stack.pop()
            y = len(queens)
            if y == n:
                res.append(queens)
                continue
            for x in range(n):
                if x not in queens and x+y not in xy_sum and x-y not in xy_diff:
                    stack.append((queens+[x], xy_sum+[x+y], xy_diff+[x-y]))
        return [['.' * i + 'Q' + '.' * (n-i-1) for i in xs] for xs in res]

# test
print(Solution().solveNQueens(4))
print(Solution().solveNQueens2(4))
