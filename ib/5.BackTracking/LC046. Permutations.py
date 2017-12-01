'''
Given a collection of numbers, return all possible permutations.

Example:

[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]
 NOTE
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection
are unique.
 Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS.
Example : next_permutations in C++ / itertools.permutations in python.
If you do, we will disqualify your submission retroactively and give you penalty
points.
'''
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, nums):
        import itertools
        return list(itertools.permutations(nums, len(nums)))

    # insert next number to anywhere
    def permute2(self, nums):
        res = [[]]
        for n in nums:
           res = [r[:i] + [n] + r[i:] for r in res for i in range(len(r)+1)]
        return sorted(res)

    # resursive take one number and add to the the permuation of the rest
    def permute3(self, nums):
        return [[n]+p for i,n in enumerate(nums)
                        for p in self.permute3(nums[:i] + nums[i+1:])] or [[]]

    # dfs recursive
    def permute4(self, nums):
        def dfs(nums, path):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], path + [nums[i]])
        res = []
        dfs(nums, [])
        return res

    # bfs
    def permute5(self, nums):
        from collections import deque
        res = []
        queue = deque([(nums, [])])
        while queue:
            nums, path = queue.popleft()
            if not nums:
                res.append(path)
                continue
            for i in range(len(nums)):
                queue.append((nums[:i] + nums[i+1:], path + [nums[i]]))
        return res

# test
print(Solution().permute([1,2,3]))
print(Solution().permute2([1,2,3]))
print(Solution().permute3([1,2,3]))
print(Solution().permute4([1,2,3]))
print(Solution().permute5([1,2,3]))
print(Solution().permute([]))
print(Solution().permute2([]))
print(Solution().permute3([]))
print(Solution().permute4([]))
print(Solution().permute5([]))
