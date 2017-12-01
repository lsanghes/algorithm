'''
A robot is located at the top-left corner of an A x B grid (marked ‘Start’ in
the diagram below).

The robot can only move either down or right at any point in time. The robot is
trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the
diagram below).

How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed
integer.

Example :

Input : A = 2, B = 2
Output : 2

2 possible routes : (0, 0) -> (0, 1) -> (1, 1)
              OR  : (0, 0) -> (1, 0) -> (1, 1)
'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer

    # n=total, steps k=horizontal steps, nCk = n!/k!(n-k)!
    def uniquePaths(self, row, col):
        from math import factorial as fact
        n = col - 1 + row - 1
        k = row - 1
        return fact(n) // (fact(k) * fact(n-k))

    # dp solution with m*n matrix.
    # grid[r][c] = number of paths to from (0,0) to (r,c)
    def uniquePaths2(self, row, col):
        grid = [[1 for _ in range(col)] for _ in range(row)]
        for r in range(1, row):
            for c in range(1, col):
                grid[r][c] = grid[r-1][c] + grid[r][c-1]
        return grid[-1][-1]

# test
print(Solution().uniquePaths(2,2))
print(Solution().uniquePaths2(2,2))
