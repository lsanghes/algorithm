'''
Write a function that takes an unsigned integer and returns the number of 1
bits it has.

Example:

The 32-bit integer 11 has binary representation

00000000000000000000000000001011
so the function should return 3.

Note that since Java does not have unsigned int, use long for Java
'''
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        res = 0
        while A > 0:
            res += A & 1 # increase count if last bit is 1
            A >>= 1 # remove the last bit, equivalent to A //= 2
        return res

    def numSetBits2(self, A):
        return bin(A)[2:].count('1')

# test
print(Solution().numSetBits(11))
print(Solution().numSetBits2(11))


