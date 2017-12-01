'''
Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return 1 ( true ).

A = [3,2,1,0,4], return 0 ( false ).

Return 0/1 for this problem
'''
class Solution:
    # if max_reach < cur_index, then it cannot move forward
    def canJump(self, nums):
        cur_index = max_reach = 0
        while max_reach >= cur_index: # must be able to reach cur_index
            max_reach = max(max_reach, cur_index + nums[cur_index])
            if max_reach >= len(nums)-1:
                return True
            cur_index += 1
        return False

    # for loop instead of while loop
    def canJump2(self, nums):
        max_reach = 0
        for cur_index, jumps in enumerate(nums):
            if cur_index > max_reach:
                return False
            max_reach = max(max_reach, cur_index + jumps)
        return True # max_reach always >= len(nums)-1 after for loop

# test
print(Solution().canJump([2,9,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))
print(Solution().canJump2([2,9,1,1,4]))
print(Solution().canJump2([3,2,1,0,4]))
