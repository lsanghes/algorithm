'''
Given an array S of n integers, are there elements a, b, c in S such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of
zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    # O(N^2)
    # first sort the array, and for each n in nums O(n)
    # use two pointer to check all possible combinations j, k from outter
    # to inner, which only takes O(n) since array is already sorted!
    # we also need to skip dup in the array
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 2): # fixing i and check possible j, k
            if i > 0 and nums[i] == nums[i-1]: # skip dup
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if cur_sum > 0:
                    k -= 1
                elif cur_sum < 0:
                    j += 1
                else:
                    res.append((nums[i], nums[j], nums[k]))
                    while j < k and nums[j] == nums[j+1]: # skip dup
                        j += 1
                    j += 1
                    while j < k and nums[k] == nums[k-1]: # skip dup
                        k -= 1
                    k -= 1
        return res

# test
print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([1,-4,0,0,5,-5,1,0,-2,4,-4,1,-1,-4,3,4,-1,-1,-3]))
