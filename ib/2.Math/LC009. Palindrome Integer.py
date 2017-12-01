'''
Determine whether an integer is a palindrome. Do this without extra space.

A palindrome integer is an integer x for which reverse(x) = x where reverse(x)
is x with its digit reversed.
Negative numbers are not palindromic.

Example :

Input : 12121
Output : True

Input : 123
Output : False
'''
class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )

    # O(1) space
    # how about int overflow??
    def isPalindrome(self, x):
        if x < 0:
            return False
        x_orig, x_rev = x, 0
        while x:
            x_rev = x_rev * 10 + x % 10
            x = x // 10
        return x_rev == x_orig

    def isPalindrome2(self, A):
        return str(A) == str(A)[::-1]

# test
print(Solution().isPalindrome(12121))
print(Solution().isPalindrome2(12121))
