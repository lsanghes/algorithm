'''
Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.
'''
class Solution:
    # @param A : list of integers
    # @return an integer

    # put number b/w 1 ~ n into position 0 ~ n-1
    # reutnr the first number not in correct position
    def firstMissingPositive(self, A):
        n = len(A)
        for i in range(n):
            # A[i]-1 is target_index
            # keep swaping if number 1 ~ n is not in target position
            # do not swap if target position has the same vale >> infinite loop
            # the answer must be <= n
            while 1 <= A[i] <= n and A[i]-1 != i and A[i] != A[A[i]-1]:
                j = A[i] - 1
                A[i], A[j] = A[j], A[i]
                # below doesn't work - A[i] is changed before calling A[A[i]-1]
                # A[i], A[A[i]-1] = A[A[i]-1], A[i]
        for i in range(n):
            if i + 1 != A[i]:
                return i + 1
        return n + 1 # array is exactly 1,2,3, ... , n

# test
print(Solution().firstMissingPositive([1,2,0]))
print(Solution().firstMissingPositive([3,4,-1,1]))
print(Solution().firstMissingPositive([-8, -7, -6]))
print(Solution().firstMissingPositive([1,2,3,4]))
