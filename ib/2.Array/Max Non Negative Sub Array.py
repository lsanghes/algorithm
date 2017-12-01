'''
Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing
the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the
sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

Example:

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]
NOTE: If there is a tie, then compare with segment's length and return segment
which has maximum length
NOTE 2: If there is still a tie, then return the segment with minimum starting
index
'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        glb_sum, cur_sum = [], []
        for a in A:
            cur_sum = cur_sum + [a] if a >= 0 else []
            cond1 = sum(cur_sum) > sum(glb_sum)
            cond2 = sum(cur_sum) == sum(glb_sum) and len(cur_sum) > len(glb_sum)
            if cond1 or cond2:
                glb_sum = cur_sum
        return glb_sum

# test
print(Solution().maxset([1, 2, 5, -7, 2, 3]))
