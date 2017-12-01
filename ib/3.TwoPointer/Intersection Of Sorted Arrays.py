'''
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]
 NOTE : For the purpose of this problem ( as also conveyed by the sample case ),
 assume that elements that appear more than once in both arrays should be
 included multiple times in the final output.
'''
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers

    # traverse from begin to end since both array is sorted
    def intersect(self, A, B):
        res = []
        ix_a = ix_b = 0
        while ix_a < len(A) and ix_b < len(B):
            a, b = A[ix_a], B[ix_b]
            if a > b:
                ix_b += 1
            elif a < b:
                ix_a += 1
            else:
                res.append(a)
                ix_a += 1
                ix_b += 1
        return res

# test
print(Solution().intersect([1,2,3,3,4,5,6],[3,5]))
