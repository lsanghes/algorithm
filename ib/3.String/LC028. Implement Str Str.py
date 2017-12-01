'''
Please Note:

Another question which belongs to the category of questions which are
intentionally stated vaguely.
Expectation is that you will ask for correct clarification or you will state
your assumptions before you start coding.

Implement strStr().

 strstr - locate a substring ( needle ) in a string ( haystack ).
Try not to use standard library string functions for this question.

Returns the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.

 NOTE: Good clarification questions:
What should be the return value if the needle is empty?
What if both haystack and needle are empty?
For the purpose of this problem, assume that the return value should be -1 in
both cases.
'''
class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0 # ib returns -1, lc return 0
        lo, hi = 0, m - n
        for i in range(lo, hi+1):
            if haystack[i:i+n] == needle:
                return i
        return -1

    # python build-in function
    def strStr2(self, haystack, needle):
        return haystack.find(needle)

# test
print(Solution().strStr('abcdef', 'de'))
print(Solution().strStr('abc', ''))
print(Solution().strStr2('abcdef', 'de'))
print(Solution().strStr2('abc', ''))
