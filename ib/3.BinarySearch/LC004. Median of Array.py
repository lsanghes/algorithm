'''
There are two sorted arrays A and B of size m and n respectively.

Find the median of the two sorted arrays ( The median of the array formed by
merging both the arrays ).

The overall run time complexity should be O(log (m+n)).

Sample Input

A : [1 4 5]
B : [2 3]

Sample Output

3
NOTE: IF the number of elements in the merged array is even, then the median is
the average of n / 2 th and n/2 + 1th element.
For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5
'''
class Solution:

    # O(log(m+n)) for findkth
    # Overall time complexitiy: O(log(m+n)+log(m+n)) = O(log(m+n))
    def findMedianSortedArrays(self, A, B):
        # KthSmallest2SortedArray.py
        def findkth(A, B, k):
            m, n = len(A), len(B)
            if m > n:
                return findkth(B, A, k)
            if m == 0:
                return B[k-1] # kth element of array B
            if k == 1:
                return min(A[0],B[0])
            i = min(k//2, m) # number of elements in shorter array
            j = k - i # number of elements in longer array
            if A[i-1] < B[j-1]: # all elements in A[:i] are smaller than kth
                return findkth(A[i:], B, k-i) # discard A[:i]
            else: # all elements in B[:j] are smaller or eqaul than kth
                  # if there is equal case, the same number is still in array A
                return findkth(A, B[j:], k-j) # discard B[:j]
        n = len(A) + len(B)
        if n % 2 == 0: # array is even size
            mid_left = findkth(A, B, (n-1)//2 + 1)
            mid_right = findkth(A, B, (n+1)//2 + 1)
            return (mid_left + mid_right ) / 2.0
        else: # array is odd size
            return findkth(A, B, (n-1)//2 + 1)

    """
    https://discuss.leetcode.com/topic/33440/9-lines-o-log-min-m-n-python/2
    log(min(m,n))
    binary search - KthSmallest2SortedArray.py
    same idea as findkth2, find i, j such that i + j = k - 1,  k is half lenth.
    and first i elements from A and first j elements from B are in kth array
    then next smallest number will be median
    """
    def findMedianSortedArrays2(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            return self.findMedianSortedArrays(B,A)
        # (m+n-1)//2 is the index of median
        # so median is the kth elements, or (kth, (k+1)th)/2.0
        k = (m+n-1)//2 + 1
        # lo and hi are guaranteed to be (0, m) for this k = median!
        lo, hi = 0, m # lo, hi = max(0, k-n-1), min(m, k)
        while lo <= hi:
            i = (lo + hi)//2
            j = k - 1 - i
            if j > 0 and i < m and B[j-1] > A[i]: # i is too small
                lo = i + 1
            elif i > 0 and j < n and A[i-1] > B[j]: # i is too big
                hi = i - 1
            else: # condition met or i,j are out of index
                next_two = sorted(A[i:i+2] + B[j:j+2])[:2]
                if (m + n) % 2 == 0:
                    return sum(next_two) / 2.0
                else:
                    return next_two[0]

# test
print(Solution().findMedianSortedArrays([1], [3, 4, 5, 6, 7, 8]))
print(Solution().findMedianSortedArrays2([1], [3, 4, 5, 6, 7, 8]))
