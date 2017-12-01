'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        val = int(str(abs(x))[::-1])
        if val > 2**31-1: 
            # stupid overflow case
            return 0
        return val if x > 0 else -val

# test
print(Solution().reverse(-123))
print(Solution().reverse(123))
