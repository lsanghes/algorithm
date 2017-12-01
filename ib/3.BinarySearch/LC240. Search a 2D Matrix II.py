'''
Write an efficient algorithm that searches for a value in an m x n matrix. This
matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''
class Solution:
    # use binary search tree starting from bottom-left or top-right
    # same as lc074
    def searchMatrix(self, A, B):
        rows, cols = len(A), len(A[0])
        r, c = rows - 1, 0
        while r >= 0 and c < cols:
            if A[r][c] < B:
                c += 1
            elif A[r][c] > B:
                r -= 1
            else:
                return True
        return False

# test
m = [[1,   4,  7, 11, 15],
     [2,   5,  8, 12, 19],
     [3,   6,  9, 16, 22],
     [10, 13, 14, 17, 24],
     [18, 21, 23, 26, 30]]
print(Solution().searchMatrix(m, 12))
print(Solution().searchMatrix(m, 20))
