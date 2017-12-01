'''
SubsetBookmark Suggest Edit
Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.
Example :

If S = [1,2,3], a solution is:

[
    [],
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 3],
    [2],
    [2, 3],
    [3],
]
'''
class Solution:
    # @param A : list of integers
    # @return a list of list of integers

    # append each number to all existing combination
    def subsets(self, nums):
        res = [[]]
        for n in nums:
            temp = []
            for r in res:
                # 1. must create a copy of r
                # 2. cannot append to res directly as we loop res
                temp.append(list(r) + [n])
            res.extend(temp)
        return res

    # exactly same implementation with list comprehension
    def subsets2(self, nums):
        res = [[]]
        for n in nums:
            res += [r+[n] for r in res]
        return res

    # N choose 0, 1, 2,.. n with itertools.combinations.
    def subsets3(self, nums):
        from itertools import combinations
        return [list(c) for i in range(len(nums)+1)
                            for c in combinations(nums, i)]

    #dfs resursive
    def subsets4(self, nums):
        def dfs(index, path):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])
        res = []
        dfs(0, [])
        return res

    #dfs iterative
    def subsets5(self, nums):
        stack = [(0, [])]
        res = []
        while stack:
            index, path = stack.pop()
            res.append(path)
            for i in range(index, len(nums)):
                stack.append((i+1, path+[nums[i]]))
        return res

# test
array = [1,2,3]
print(Solution().subsets(array))
print(Solution().subsets2(array))
print(Solution().subsets3(array))
print(Solution().subsets4(array))
print(Solution().subsets5(array))
