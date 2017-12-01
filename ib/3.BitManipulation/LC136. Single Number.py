'''
Given an array of integers, every element appears twice except for one. Find
that single one.

Note: Your algorithm should have a linear runtime complexity. Could you
implement it without using extra memory?

Example :

Input : [1 2 2 3 1]
Output : 3
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer

    # XOR properties.py
    # 0^n^n^m = 0^(n^n^m) = n^n^m = 0^m = m
    def singleNumber(self, A):
        n = 0
        for a in A:
            n ^= a
        return n

# test
print(Solution().singleNumber([1,2,2,3,1]))
print(Solution().singleNumber([0]))
