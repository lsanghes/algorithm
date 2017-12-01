'''
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if
reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least
starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"
'''
class Solution:
    # O(N^2) find longest palindrome from inner to outer
    # j, k are middle index
    def longestPalindrome(self, s):
        def longest(s, j, k):
            while j>=0 and k<len(s) and s[j] == s[k]:
                j, k = j-1, k+1
            return s[j+1:k]
        res = ''
        for i in range(len(s)):
            odd = longest(s, i, i) # look for odd palindrome
            even = longest(s, i, i+1) # look for even palindrome
            res = max((res, odd, even), key=lambda x:len(x))
        return res

    # still O(N^2) but A == A[::-1] is much faster
    # when s increased by 1, the length palindrome can increase by only 0, 1, 2
    def longestPalindrome2(self, s):
        start, max_len = 0, 1
        for i in range(1, len(s)):
            k2 = i-(max_len+2)+1 # starting index of palindrome with len+2
            k1 = i-(max_len+1)+1 # starting index of palindrome with len+1
            # only check len+1 if len+2 is not palindrome
            if  k2 >= 0 and s[k2:i+1] == s[k2:i+1][::-1]:
                start, max_len = k2, max_len + 2
            elif k1 >= 0 and s[k1:i+1] == s[k1:i+1][::-1]:
                start, max_len = k1, max_len + 1
        return s[start:start+max_len]

# test
print(Solution().longestPalindrome('abba'))
print(Solution().longestPalindrome2('abba'))
