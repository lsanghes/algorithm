'''
Write a function to find the longest common prefix string amongst an array of
strings.

Longest common prefix for a pair of strings S1 and S2 is the longest string S
which is the prefix of both S1 and S2.

As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Given the array of strings, you need to find the longest S which is the prefix
of ALL the strings in the array.

Example:

Given the array as:
[
  "abcdefgh",
  "aefghijk",
  "abcefgh"
]
The answer would be “a”.
'''
class Solution:
    # zip up to min len
    def longestCommonPrefix(self, strs):
        res = ''
        # zip(*str) = zip(str[0], str[1], ..., str[n])
        for chars in zip(*strs): # zip up to shortest string.
            if len(set(chars)) > 1: # chars is tuple
                break
            res += chars[0]
        return res

    # faster just compare min and max lexical elements
    def longestCommonPrefix2(self, strs):
        if not strs:
            return ''
        res = ''
        # str comparison is decided by lexical order not length!
        for a, b in zip(min(strs), max(strs)):
            if a != b:
                break
            res += a
        return res

#test
print(Solution().longestCommonPrefix(['abcdefgh','aefghijk','abcefgh']))
print(Solution().longestCommonPrefix2(['abcdefgh','aefghijk','abcefgh']))
