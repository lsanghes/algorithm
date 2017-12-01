'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution:
    # resursive solution...
    def partition(self, s):
        res = []
        for i in range(len(s)):
            pre = s[:i+1]
            if pre == pre[::-1]:
                for rest in self.partition(s[i+1:]):
                    partition = [pre] + rest
                    res.append(partition)
        return res or [[]]

    # recursive one liner with list comprehension
    def partition2(self, s):
        return [[s[:i+1]]+rest for i in range(len(s)) if s[:i+1]==s[:i+1][::-1]
                                  for rest in self.partition2(s[i+1:])] or [[]]

    # recursive dfs
    def partition3(self, s):
        def dfs(s, path):
            if not s:
                res.append(path)
                return
            for i in range(len(s)):
                if s[:i+1] == s[:i+1][::-1]:
                    dfs(s[i+1:], path+[s[:i+1]])
        res = []
        dfs(s, [])
        return res

    # iterative dfs
    def partition4(self, s):
        stack = [(s, [])]
        res = []
        while stack:
            substr, path = stack.pop()
            if not substr:
                res.append(path)
                continue
            for i in range(len(substr)):
                if substr[:i+1] == substr[:i+1][::-1]:
                    stack.append((substr[i+1:], path+[substr[:i+1]]))
        return res

# test
for s in ['aab', '']:
    print(Solution().partition(s))
    print(Solution().partition2(s))
    print(Solution().partition3(s))
    print(Solution().partition4(s))
