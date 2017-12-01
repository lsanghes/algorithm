'''
Given a digit string, return all possible letter combinations that the number
could represent.

A mapping of digit to letters (just like on the telephone buttons) is given
below.
The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.

Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Make sure the returned strings are lexicographically sorted.
'''
class Solution:
    # @param A : string
    # @return a list of strings

    # cartisan product using itertools
    def letterCombinations(self, digits):
        import itertools
        if not digits:
            return []
        numpad = ['0','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        product = itertools.product(*[numpad[int(d)] for d in digits])
        return [''.join(p) for p in product]

    # append next letter to all existing combinations
    def letterCombinations2(self, digits):
        if not digits:
            return []
        numpad = ['0','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res = ['']
        for d in digits:
            res = [r+char for r in res for char in numpad[int(d)]]
        return res

    # bfs - correct lexicographical order
    def letterCombinations4(self, digits):
        from collections import deque
        if not digits:
            return []
        numpad = ['0','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res = []
        queue = deque([(0, '')]) # initial index = 0, initial path = ''
        while queue:
            index, path = queue.popleft()
            if len(path) == len(digits):
                res.append(path)
                continue
            for char in numpad[int(digits[index])]:
                queue.append((index+1, path+char))
        return res

    # dfs - automatically take care of the lexicographical order
    def letterCombinations3(self, digits):
        def dfs(index, path):
            if index == len(digits):
                res.append(path)
                return
            for char in numpad[int(digits[index])]:
                dfs(index+1, path+char)
        if not digits:
            return []
        numpad = ['0','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res = []
        dfs(0, '') # initial index = 0, initial path = ''
        return res

# test
for digits in ('23', ''):
    print(Solution().letterCombinations(digits))
    print(Solution().letterCombinations2(digits))
    print(Solution().letterCombinations3(digits))
    print(Solution().letterCombinations4(digits))
