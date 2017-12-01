'''
Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''
class Solution:
    # @param A : string
    # @return an integer

    # remove non-alphanumeric - RegexCheatsheet.py
    def isPalindrome(self, A):
        import re
        s = re.sub('\W+', '', A).lower() # "\W" matches non-alphanumeric
        return s == s[::-1]

    # compare from outer to inner and skip non-alphanumeric
    def isPalindrome2(self, A):
        A = A.lower()
        lo, hi = 0, len(A) - 1
        while lo < hi:
            if not A[lo].isalnum():
                lo += 1
            elif not A[hi].isalnum():
                hi -= 1
            elif A[hi] == A[lo] :
                lo += 1
                hi -= 1
            else:
                return False
        return True

# test
print(Solution().isPalindrome('A man, a plan, a canal: Panama'))
print(Solution().isPalindrome2('A man, a plan, a canal: Panama'))
