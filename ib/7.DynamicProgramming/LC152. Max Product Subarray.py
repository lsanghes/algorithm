'''
Find the contiguous subarray within an array (containing at least one number)
which has the largest product.
Return an integer corresponding to the maximum product possible.

Example :

Input : [2, 3, -2, 4]
Return : 6

Possible with [2, 3]
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    # dp - similar to lc121 maximum subarray
    # keep a local min for negative number it may flip to max product
    def maxProduct(self, nums):
        global_max = local_max = local_min = nums[0]
        for n in nums[1:]:
            products = n, n*local_max, n*local_min
            local_max, local_min = max(products), min(products)
            global_max = max(global_max, local_max)
        return global_max

# test
print(Solution().maxProduct([2, 3, -2, 4]))
