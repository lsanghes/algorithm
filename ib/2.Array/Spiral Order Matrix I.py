'''
Given a matrix of m * n elements (m rows, n columns), return all elements of
the matrix in spiral order.

Example:

Given the following matrix:

[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
You should return

[1, 2, 3, 6, 9, 8, 7, 4, 5]
'''
class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    # distructive - poping the items after visiting
    def spiralOrder(self, A):
        res = []
        A = list(A) # convert tuple to list
        while A:
            # top
            res.extend(A.pop(0) if A else [])
            # right
            res.extend([a.pop() for a in A if a])
            # buttom
            res.extend(A.pop()[::-1] if A else [])
            # left
            res.extend([a.pop(0) for a in A[::-1] if a])
        return res

# test
print(Solution().spiralOrder([[ 1, 2, 3 ],
                              [ 4, 5, 6 ],
                              [ 7, 8, 9 ]]))
