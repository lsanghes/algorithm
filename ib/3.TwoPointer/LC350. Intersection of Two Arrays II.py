'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both
arrays. The result can be in any order.
Follow up:
-What if the given array is already sorted? How would you optimize your
algorithm?
-What if nums1's size is small compared to nums2's size? Which algorithm is
better?
-What if elements of nums2 are stored on disk, and the memory is limited such
that you cannot load all elements into the memory at once?
'''
class Solution:
    # use counter to find common elements
    def intersect(self, nums1, nums2):
        from collections import Counter
        c1, c2 = Counter(nums1), Counter(nums2)
        res = []
        for num, count in (c1 & c2).items(): # intersection:min(c1[x], c2[x])
            res.extend([num] * count)
        return res

    # if array is sorted, then we can re-use Intersection Of Sorted Arrays.py
    def intersect2(self, A, B):
        A.sort()
        B.sort()
        res = []
        ix_a = ix_b = 0
        while ix_a < len(A) and ix_b < len(B):
            a, b = A[ix_a], B[ix_b]
            if a > b:
                ix_b += 1
            elif a < b:
                ix_a += 1
            else:
                res.append(a)
                ix_a += 1
                ix_b += 1
        return res

# test
print(Solution().intersect([2, 1], [1, 1]))
print(Solution().intersect2([2, 1], [1, 1]))
print(Solution().intersect([1, 2, 3, 3, 4, 5, 6], [3, 5]))
print(Solution().intersect2([1, 2, 3, 3, 4, 5, 6], [3, 5]))
