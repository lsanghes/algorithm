'''
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        cur_max = glb_max = A[0]
        for num in A[1:]:
            if cur_max < 0:
                cur_max = 0
            cur_max += num
            glb_max = max(glb_max, cur_max)
        return glb_max

# test
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
