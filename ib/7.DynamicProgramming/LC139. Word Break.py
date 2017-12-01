'''
Given a string s and a dictionary of words dict, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''
class Solution:
    #dp
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if type(wordDict) != type(set()): # IB
            wordDict = set(wordDict)
        dp = [False] * (len(s) + 1) # dp[i] indicates if s[:i] is breakable
        dp[0] = True
        for k in range(1, len(s)+1):
            # reversed faster in most test cases
            # non-reversed version timeout in IB
            for j in reversed(range(k)):
                if dp[j] and s[j:k] in wordDict:
                    dp[k] = True
                    break # found at least 1 break, move to next k
        return dp[-1]

    # actually we just need to store the index where a match is found
    def wordBreak2(self, s, wordDict):
        if type(wordDict) != type(set()): # IB
            wordDict = set(wordDict)
        dp = [0] # each i in dp indicates if s[:i] is breakable
        for k in range(1, len(s)+1):
            # no need to loop through all range(k)
            # only loop trhough breakable points, i.e. previous Ks
            for j in reversed(dp):
                if s[j:k] in wordDict:
                    dp.append(k)
                    break # found at least 1 break, move to next k
        return dp[-1] == len(s)

# test
print(Solution().wordBreak("leetcode", ["leet", "code"]))
print(Solution().wordBreak("leetcode", ["lee", "code"]))
print(Solution().wordBreak("bb", ["a","b","bbb","bbbb"]))
print(Solution().wordBreak("aaaaaaa", ["aaaa","aaa"]))
print(Solution().wordBreak2("leetcode", ["leet", "code"]))
print(Solution().wordBreak2("leetcode", ["lee", "code"]))
print(Solution().wordBreak2("bb", ["a","b","bbb","bbbb"]))
print(Solution().wordBreak2("aaaaaaa", ["aaaa","aaa"]))
