'''
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
class Solution(object):
    # O(N^2)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for j in range(len(nums)):
            for k in range(j+1, len(nums)):
                if nums[j] + nums[k] == target:
                    return j, k

    # O(N)
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        memo = {}
        for i in range(len(nums)):
            if nums[i] in memo:
                return memo[nums[i]], i
            elif target-nums[i] not in memo:
                # ensure that minimum index1 is returned if there are multiple
                # solutions with the minimum index2
                memo[target-nums[i]] = i
# test
print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum2([2,7,11,15], 9))
