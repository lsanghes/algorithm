'''
Given a column title as appears in an Excel sheet, return its corresponding
column number.

Example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
'''
class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        letters = '.ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = 0
        for i in range(len(A)):
            val = letters.index(A[i])
            power = len(A) - i - 1
            res += val * (26 ** power)
        return res

    # use dict instead of list.index()
    def titleToNumber2(self, A):
        d = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', list(range(1, 27))))
        res = 0
        for i in range(len(A)):
            val = d[A[i]]
            power = len(A) - i - 1
            res += val * (26 ** power)
        return res

# test
print(Solution().titleToNumber('AAA'))
print(Solution().titleToNumber('ABC'))
print(Solution().titleToNumber2('AAA'))
print(Solution().titleToNumber2('ABC'))
