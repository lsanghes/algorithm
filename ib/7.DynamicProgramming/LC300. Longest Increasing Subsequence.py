'''
Find the longest increasing subsequence of a given sequence / array.

In other words, find a subsequence of array in which the subsequence’s elements
are in strictly increasing order, and in which the subsequence is as long as
possible. This subsequence is not necessarily contiguous, or unique. In this
case, we only care about the length of the longest increasing subsequence.

Example :

Input : [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Output : 6
The sequence : [0, 2, 6, 9, 13, 15]
            or [0, 4, 6, 9, 11, 15]
            or [0, 4, 6, 9, 13, 15]
'''
class Solution:
    # binary search O(nlogn)
    # keep track of longest sequence with the smallest possible numbers in it
    def lis(self, A):
        from bisect import bisect_left
        if not A: return 0
        inc = [A[0]]
        for i, n in enumerate(A[1:]):
            if n > inc[-1]:
                inc.append(n)
            else:
                inc[bisect_left(inc, n)] = n
        return len(inc)

    # DP O(N^2) 19200ms
    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [1]*len(nums)
        for right in range (1, len(nums)):
            for left in range(right):
                if nums[right] > nums[left]:
                    dp[right] = max(dp[right], dp[left]+1)
        return max(dp)

# test
print(Solution().lis([1,4,2,6,5,4,3]))
print(Solution().lengthOfLIS2([1,4,2,6,5,4,3]))
