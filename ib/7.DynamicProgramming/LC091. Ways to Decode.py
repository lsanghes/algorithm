'''
A message containing letters from A-Z is being encoded to numbers using the
following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways
to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''
class Solution:
    # DP - time O(n), space O(n)
    # string s can be decoded in two ways:
    # decode s excluding last 2 char - when last 2 char forms a valid num
    # decode s excluding last 1 char - when last 1 char forms a valid num
    def numDecodings(self, s):
        if not s:
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i >= 2 and '10' <= s[i-2:i] <= '26':
                dp[i] += dp[i-2]
        return dp[n]

    # DP - time O(n), space O(1)
    # just have to track dp2 and dp1 instead of entire array
    def numDecodings2(self, s):
        if not s or s[0] == '0':
            return 0
        dp2 = None
        dp1 = 1
        for i in range(1, len(s)+1):
            cur = 0
            if s[i-1] != '0':
                cur += dp1
            if i >= 2 and '10' <= s[i-2:i] <= '26':
                cur += dp2
            dp2, dp1 = dp1, cur
        return dp1

# test
print(Solution().numDecodings("123"))
print(Solution().numDecodings("220726"))
print(Solution().numDecodings2("123"))
print(Solution().numDecodings2("220726"))
