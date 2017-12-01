'''
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element
appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change
the original array as well in place

Do not allocate extra space for another array, you must do this in place with
constant memory.

 Example:
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
'''
class Solution:
    # @param A : list of integers
    # @return an integer

    # j number of unique items
    # the result of A[:j] is the sorted array without dup
    def removeDuplicates(self, A):
        if not A:
            return 0
        j, k = 1, 1
        while j<len(A) and k<len(A):
            if A[k] != A[k-1]:
                A[j] = A[k]
                j += 1
                k += 1
            else:
                k += 1
        return j

# test
print(Solution().removeDuplicates([1,1,1,2,2,3,4,4,5]))
