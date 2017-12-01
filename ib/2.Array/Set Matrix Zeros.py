'''
Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and
column to 0.

Do it in place.

Example

Given array A as

1 0 1
1 1 1
1 1 1
On returning, the array A should be :

0 0 0
1 0 1
1 0 1
Note that this will be evaluated on the extra memory used. Try to minimize the
space and time complexity.
'''
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        row, col = len(A), len(A[0])
        # 1 memo - find out if 1st row and 1st column contain any 0
        top_row_zero = True if sum(A[0]) < col else False
        left_col_zero = True if sum([r[0] for r in A]) < row else False
        # 2 use first column to track if the row contains any 0.
        for r in range(1, row):
            if sum(A[r]) < col:
                A[r][0] = 0
        # 3 use first row to track if the column contains any 0
        for c in range(1, col):
            if sum([r[c] for r in A]) < row:
                A[0][c] = 0
        # 4 update the rest of rows if needed. 4 & 5 must be after both 2 & 3
        for r in range(1, row):
            if A[r][0] == 0:
                A[r] = [0] * col
        # 5 update the rest of colmuns if needed
        for c in range(1, col):
            if A[0][c] == 0:
                for r in range(row):
                    A[r][c]=0
        # 6 update first row and column base on initial memo
        if top_row_zero:
            A[0] = [0] * col
        if left_col_zero:
            for r in A:
                r[0]=0
        return A

# test
print(Solution().setZeroes([[1,0,1],
                            [1,1,1],
                            [1,1,1]]))
