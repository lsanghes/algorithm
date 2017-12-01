'''
Print concentric rectangular pattern in a 2d matrix.
Let us show you some examples to clarify what we mean.

Example 1:

Input: A = 4.
Output:

4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
Example 2:

Input: A = 3.
Output:

3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3
The outermost rectangle is formed by A, then the next outermost is formed by
A-1 and so on.

You will be given A as an argument to the function you need to implement, and
you need to return a 2D array.
'''
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        n = 2 * A - 1 # n x n matrix
        matrix = [[0] * n for _ in range(n)]
        for num in reversed(range(1, A+1)):
            # the boundaries of current num
            top = left = A - num
            bottom = right = n - 1 - top
            for i in range(left, right+1):
                matrix[top][i] = num
                matrix[i][left] = num
                matrix[bottom][i] = num
                matrix[i][right] = num
        return matrix

# test
print(Solution().prettyPrint(3))
print(Solution().prettyPrint(4))
