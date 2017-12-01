'''
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array will not contain duplicates.

NOTE 1: Also think about the case when there are duplicates. Does your current
solution work? How does the time complexity change?*
PROBLEM APPROACH:

Note: If you know the number of times the array is rotated, then this problem
becomes trivial. If the number of rotation is x, then minimum element is A[x].
Lets look at how we can calculate the number of times the array is rotated.
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer

    # if A[i] > A[-1], right part is out-of-order, smallest number is in A[i+1:]
    # if A[i] <= A[-1], right part is in-order, smallest number is in A[:i+1]
    def findMin(self, A):
        lo, hi = 0, len(A) - 1
        while lo < hi: # condition should be < instead of <=
            mid = (lo + hi)//2
            if A[mid] > A[hi]:
                lo = mid + 1
            else:
                hi = mid
        return A[lo]

# test
print(Solution().findMin([0,1,2,3,4,5,6]))
print(Solution().findMin([6,0,1,2,3,4,5]))
print(Solution().findMin([5,6,0,1,2,3,4]))
print(Solution().findMin([4,5,6,0,1,2,3]))
print(Solution().findMin([3,4,5,6,0,1,2]))
print(Solution().findMin([2,3,4,5,6,0,1]))
print(Solution().findMin([1,2,3,4,5,6,0]))
