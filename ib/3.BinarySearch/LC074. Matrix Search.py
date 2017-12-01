'''
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of
the previous row.
Example:

Consider the following matrix:

[
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return 1 ( 1 corresponds to true )

Return 0 / 1 ( 0 if the element is not present, 1 if the element is present )
for this problem
'''
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer

    # binary search
    def searchMatrix(self, A, B):
        rows, cols = len(A), len(A[0])
        lo, hi = 0, rows * cols - 1
        while lo <= hi:
            mid = (lo + hi)//2
            val = A[mid // cols][mid % cols]
            if val > B:
                hi = mid - 1
            elif val < B:
                lo = mid + 1
            else:
                return True
        return False

    # use binary search tree starting from bottom-left or top-right
    def searchMatrix2(self, A, B):
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
m = [[1,   3,  5,  7],
     [10, 11, 16, 20],
     [23, 30, 34, 50]]
for i in range(10):
    print(Solution().searchMatrix(m, i) == Solution().searchMatrix2(m, i))
