'''
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of
distinct solutions.

'''
class Solution:
    # dfs resursive
    def totalNQueens(self, n):
        def dfs(queens, xy_sum, xy_diff):
            y = len(queens) # next row we need to work on
            if y == n:
                res[0] += 1
                return
            for x in range(n): # each row has n choices
                if x not in queens and y+x not in xy_sum and x-y not in xy_diff:
                    dfs(queens+[x], xy_sum+[y+x], xy_diff+[x-y])
        res = [0] # can't modify non-mutable outside the dfs()
        dfs([], [], [])
        return res[0]

    #dfs iterative
    def totalNQueens2(self, n):
        res = 0
        stack = [([], [], [])]
        while stack:
            queens, xy_sum, xy_diff = stack.pop()
            y = len(queens)
            if y == n:
                res += 1
                continue
            for x in range(n):
                if x not in queens and x+y not in xy_sum and x-y not in xy_diff:
                    stack.append((queens+[x], xy_sum+[x+y], xy_diff+[x-y]))
        return res

# test
print(Solution().totalNQueens(10))
print(Solution().totalNQueens2(10))
