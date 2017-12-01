'''
Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right which minimizes the sum of all numbers along its path.

 Note: You can only move either down or right at any point in time.
Example :

Input :

    [  1 3 2         [  1  4  6
       4 3 1            5  7  7
       5 6 1            10 13 8
    ]                ]

Output : 8
     1 -> 3 -> 2 -> 1 -> 1
'''
class Solution:
    # dp
    # populate the total distance for first row and first column
    # grid[r][c] += min(grid[r][c-1], grid[r-1][c])
    def minPathSum(self, grid):
        rows, cols = len(grid), len(grid[0])
        for c in range(1, cols):
            grid[0][c] += grid[0][c-1]
        for r in range(1, rows):
            grid[r][0] += grid[r-1][0]
        for r in range(1, rows):
            for c in range(1, cols):
                grid[r][c] += min(grid[r][c-1], grid[r-1][c])
        return grid[-1][-1]

    # dfs/bfs bruteforce check all combination - TLE
    def minPathSum2(self, grid):
        queue = [(0, 0, grid[0][0])]
        min_path_sum = float("inf")
        while queue:
            row, col, path_sum = queue.pop()
            if row == len(grid)-1 and col == len(grid[0]) - 1:
                min_path_sum = min(min_path_sum, path_sum)
                continue
            for dr, dc in [(0,1),(1,0)]:
                nr = row + dr
                nc = col + dc
                if nr <= len(grid)-1 and nc <= len(grid[0])-1:
                    queue.append((nr, nc, path_sum + grid[nr][nc]))
        return min_path_sum

# test
print(Solution().minPathSum([[1, 3, 2], [4, 3, 1], [5, 6, 1]]))
print(Solution().minPathSum2([[1, 3, 2], [4, 3, 1], [5, 6, 1]]))
