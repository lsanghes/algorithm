'''
Given a sorted array of integers, find the number of occurrences of a given
target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return 0

**Example : **
Given [5, 7, 7, 8, 8, 10] and target value 8,
return 2.

PROBLEM APPROACH :
'''
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    # find the first and last occurance of the number
    def findCount(self, A, B):
        # find the left most target
        first_occ = last_occ = None
        low, high = 0, len(A)-1
        while low <= high:
            mid = (low + high)//2
            if A[mid] > B:
                high = mid - 1
            elif A[mid] < B:
                low = mid + 1
            else:
                first_occ = mid
                high = mid - 1
        # stop if target is not found
        if not first_occ:
            return 0
        # find the right most target
        low, high = first_occ, len(A)-1
        while low <= high:
            mid = (low + high)//2
            if A[mid] > B:
                high = mid - 1
            elif A[mid] < B:
                low = mid + 1
            else:
                last_occ = mid
                low = mid + 1
        return last_occ - first_occ + 1

    # using bisect
    def findCount2(self, A, B):
        from bisect import bisect_left, bisect_right
        first = bisect_left(A, B)
        last = bisect_right(A, B)
        return 0 if last == first else last - first

# test
print(Solution().findCount([5, 7, 7, 8, 8, 10], 8))
print(Solution().findCount([5, 7, 7, 8, 8, 10], 6))
print(Solution().findCount2([5, 7, 7, 8, 8, 10], 8))
print(Solution().findCount2([5, 7, 7, 8, 8, 10], 6))
