'''
Question: Given an array of positive numbers, find the maximum sum of a
subsequence with the constraint that no 2 numbers in the sequence should be
adjacent in the array. So 3 2 7 10 should return 13 (sum of 3 and 10) or 3 2 5
10 7 should return 15 (sum of 3, 5 and 7).Answer the question in most efficient
way.
'''

# DP FindMaxSum[i] = max(FindMaxSum[i-2]+arr[i],FindMaxSum[i-1]) when i>=2
def FindMaxSum(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    pre2 = nums[0]
    pre1 = nums[1]
    for i in range(2, n):
        cur = max(pre2 + nums[i], pre1)
        pre2, pre1 = max(pre2, pre1), cur
    return cur

# more concisely
def FindMaxSum(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    prev = nums[0]
    cur = nums[1]
    for i in range(2, n):
        prev, cur = max(prev, cur), prev + nums[i]
    return max(prev, cur)

# test
print(FindMaxSum([1,9,3,4,2,2,4]))
print(FindMaxSum([16,5,36,82,1]))

'''
Given a 2 * N Grid of numbers, choose numbers such that the sum of the numbers
is maximum and no two chosen numbers are adjacent horizontally, vertically
or diagonally, and return it.

Example:

Grid:
    1 2 3 4
    2 3 4 5
so we will choose
3 and 5 so sum will be 3 + 5 = 8

Note that you can choose more than 2 numbers
'''
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, lists):
        A, B = lists[0], lists[1]
        n = len(A)
        if n == 0:
            return 0
        if n == 1:
            return max(A[0], B[0])
        prev = max(A[0], B[0])
        cur = max(A[1], B[1])
        for i in range(2, n):
            prev, cur = max(prev, cur), prev + max(A[i],B[i])
        return max(prev,cur)

# test
print(Solution().adjacent([[1, 2, 3, 4],
                           [2, 3, 4, 5]]))
print(Solution().adjacent([[16, 5, 54, 55, 36, 82, 61, 77, 66, 61],
                           [31, 30, 36, 70, 9, 37, 1, 11, 68, 14]]))
