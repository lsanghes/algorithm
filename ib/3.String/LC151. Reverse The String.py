'''
Given an input string, reverse the string word by word.

Example:

Given s = "the sky is blue",

return "blue is sky the".

A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it
is present in the input string.
If there are multiple spaces between words, reduce them to a single space in
the reversed string.
'''

class Solution:
    # @param A : string
    # @return string

    # split() take of multiple whitespace automatically.
    # split(' ') only split by ONE space
    def reverseWords(self, A):
        return ' '.join(A.strip().split()[::-1])

# test
print(Solution().reverseWords('the sky is blue'))
