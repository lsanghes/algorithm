'''
Find the kth smallest element in an unsorted array of non-negative integers.

Definition of kth smallest element

 kth smallest element is the minimum possible n such that there are atleast k
 elements in the array <= n.
In other words, if the array A was sorted, then A[k - 1] ( k is 1 based, while
the arrays are 0 based )
NOTE
You are not allowed to modify the array ( The array is read only ).
Try to do it using constant extra space.

Example:

A : [2 1 4 3 2]
k : 3

answer : 2
'''
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, k):
        return sorted(A)[k-1]

    # inplace quick select - distructive
    def kthsmallest2(self, A, k):
        import random
        # QuickSortPartition.py
        def partition(A, lo, hi):
            pivot_ix = hi # use last element as pivot
            divider_ix = lo # use first element as divider
            for i in range(lo, hi):
                if A[i] < A[pivot_ix]:
                    A[i], A[divider_ix] = A[divider_ix], A[i]
                    divider_ix += 1
            # after for loop, all elements in A[:divider_ix] is < A[pivot_ix]
            # ie. pivot should be in the position of divider_ix
            A[pivot_ix], A[divider_ix] = A[divider_ix], A[pivot_ix]
            # everything on the left of pivot is smaller than pivot
            # everything on the right of pivot is bigger or equal than pivot
            return divider_ix

        A = list(A) # ib input is tuples.
        random.shuffle(A) # random shuffle ensure O(nlogn) on average
        if 1 <= k <= len(A): # this ensure function always return
            lo, hi = 0, len(A)-1
            while True:
                pivot_ix = partition(A, lo, hi)
                if pivot_ix > k - 1:
                    hi = pivot_ix - 1
                elif pivot_ix < k - 1:
                    lo = pivot_ix + 1
                else:
                    return A[pivot_ix]

# test
A = [9,4,1,8,7,6,3,2,5]
for i in range(1, len(A)+1):
    print(Solution().kthsmallest(A, i))
    print(Solution().kthsmallest2(A, i))
