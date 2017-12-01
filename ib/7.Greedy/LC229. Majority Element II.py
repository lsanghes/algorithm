'''
Given an integer array of size n, find all elements that appear more than ⌊n/3⌋
times. The algorithm should run in linear time and in O(1) space.
'''
class Solution:
    # Moore's voting algorithm: keep track of two counters!
    # same algorithm as lc169
    # additional edge case in checking num not in candidates
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts, candidates = [0, 0], [None, None]
        for num in nums:
            if counts[0] == 0 and num not in candidates: # new candidate
                candidates[0], counts[0] = num, 1
            elif counts[1] == 0 and num not in candidates: # new candidate
                candidates[1], counts[1] = num, 1
            elif candidates[0] == num: # existing candidate
                counts[0] += 1
            elif candidates[1] == num: # existing candidate
                counts[1] += 1
            else: # existing candidate
                counts[0] -= 1
                counts[1] -= 1
        return [c for c in candidates if nums.count(c) > len(nums)//3]

    # tweak the sequence of condition to remove the edge case
    def majorityElement2(self, nums):
        counts, candidates = [0, 0], [None, None]
        for num in nums:
            if candidates[0] == num:
                counts[0] += 1
            elif candidates[1] == num:
                counts[1] += 1
            elif not counts[0]:
                candidates[0], counts[0] = num, 1
            elif not counts[1]:
                candidates[1], counts[1] = num, 1
            else:
                counts[0] -= 1
                counts[1] -= 1
        return [c for c in candidates if nums.count(c) > len(nums)//3]

    # a generic algorithm for any n/k times
    def majorityElementGeneric(self, nums, k):
        def helper(counts, candidates, num):
            for i, candidate in enumerate(candidates):
                if candidate == num:
                    counts[i] += 1
                    return
            for i, count in enumerate(counts):
                if count == 0:
                    candidates[i], counts[i] = num, 1
                    return
            for i, count in enumerate(counts):
                counts[i] -= 1

        counts = [0] * (k-1)
        candidates = [None] * (k-1)
        for num in nums:
            helper(counts, candidates, num)
        return [c for c in candidates if nums.count(c) > len(nums)//k]

# test
print(Solution().majorityElement([4,3,5,3]))
print(Solution().majorityElement([1,2,2,3,2,1,1,3]))
print(Solution().majorityElement([1,1,1,1,2,2,2,2,3,3]))
print(Solution().majorityElement2([4,3,5,3]))
print(Solution().majorityElement2([1,2,2,3,2,1,1,3]))
print(Solution().majorityElement2([1,1,1,1,2,2,2,2,3,3]))
print(Solution().majorityElementGeneric([4,3,5,3], 3))
print(Solution().majorityElementGeneric([1,2,2,3,2,1,1,3], 3))
print(Solution().majorityElementGeneric([1,1,1,1,2,2,2,2,3,3], 3))
