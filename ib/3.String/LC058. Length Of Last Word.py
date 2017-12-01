'''
Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space
characters only.

Example:

Given s = "Hello World",

return 5 as length("World") = 5.

Please make sure you try to solve this problem without using library functions.
Make sure you only traverse the string once.
'''
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        s = A.strip()
        i = len(s) - 1
        while i >= 0:
            if s[i] == ' ':
                return len(s) - 1 - i
            i -= 1
        return len(s)

    def lengthOfLastWord2(self, s):
        s = s.strip()
        return len(s.split()[-1]) if s else 0

# test
print(Solution().lengthOfLastWord('hello World'))
print(Solution().lengthOfLastWord2('hello World'))
