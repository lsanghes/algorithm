'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''
class Solution:
    # swap two elements from outer to inner
    def reverseString(self, s):
        lo, hi = 0, len(s)-1
        s = list(s) # str does not support index assignment
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1
        return ''.join(s)

    # python reverse
    def reverseString2(self, s):
        return s[::-1]

# test
print(Solution().reverseString('i am lin sang'))
print(Solution().reverseString2('i am lin sang'))
