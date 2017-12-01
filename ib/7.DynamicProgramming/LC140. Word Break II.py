'''
Given a string s and a dictionary of words dict, add spaces in s to construct a
sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
'''
class Solution:
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: List[str]
    """
    # simple dfs - TLE
    def wordBreak(self, s, wordDict):
        # loop through s to match wordDict, faster if dictionary is large
        def dfs(s, path):
            if not s:
                res.append(' '.join(path))
            for i in range(1, len(s)+1):
                word = s[:i]
                if word in wordDict:
                    dfs(s[i:], path+[word])
        # loop through wordDict to match s, faster if s is large
        def dfs2(s, path):
            if not s:
                res.append(' '.join(path))
            for word in wordDict:
                if s[:len(word)] == word:
                    dfs2(s[len(word):], path+[word])
        res = []
        dfs(s, [])
        return res

    # dfs + dp - AC solution
    def wordBreak2(self, s, wordDict):
        # loop through s to match wordDict, faster if dictionary is large
        def dfs(s):
            if not s: return ['']
            if s in dp: return dp[s]
            res = []
            for i in range(1, len(s)+1):
                word = s[:i]
                if word in wordDict:
                    for r in dfs(s[i:]):
                        res.append((word + ' ' + r) if r else word)
            dp[s] = res
            return res
        # loop through wordDict to match s, faster if s is large
        def dfs2(s):
            if not s: return ['']
            if s in dp: return dp[s]
            res = []
            for word in wordDict:
                if s[:len(word)] == word:
                    for r in dfs2(s[len(word):]):
                        res.append((word + ' ' + r) if r else word)
            dp[s] = res
            return res
        dp = {}
        return dfs(s)

# test
print(Solution().wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"]))
print(Solution().wordBreak2("catsanddog",["cat", "cats", "and", "sand", "dog"]))
