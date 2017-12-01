'''
Given a number N >= 0, find its representation in binary.

Example:

if N = 6,

binary form = 110
'''
class Solution:
    # @param A : integer
    # @return a strings
    # http://www.wikihow.com/Convert-from-Decimal-to-Binary
    def findDigitsInBinary(self, A):
        if A == 0:
            return '0'
        res = ''
        while A:
            res = str(A % 2) + res
            A = A // 2
        return res

    def findDigitsInBinary2(self, A):
        return bin(A)[2:] # eg: 18 = 0b10010

# test
for n in range(1, 20):
    binary = Solution().findDigitsInBinary(n)
    print('{} : {}'.format(n, binary))
    binary2 = Solution().findDigitsInBinary2(n)
    print('{} : {}'.format(n, binary2))
