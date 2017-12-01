'''
Given an array of size n, find the majority element. The majority element is
the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always
exist in the array.
'''
class Solution:
    # use collection counter
    def majorityElement(self, nums):
        from collections import Counter
        counter = Counter(nums)
        candidate, count = counter.most_common(1)[0]
        return candidate if count > len(nums)//2 else None

    # median should always be majority if majority exist!
    def majorityElement2(self, nums):
        candidate = sorted(nums)[len(nums)//2]
        return candidate if nums.count(candidate) > len(nums)//2 else None

    # Moore's voting algorithm: constant space complexity
    # find element with most count in one pass
    # if the counter is 0, set the current candidate to x and the counter to 1.
    # If the counter is not 0, increment or decrement the counter based on
    # whether x is the current candidate.
    # last determine if candidate is the majority
    def majorityElement3(self, nums):
        candidate, count = None, 0
        for num in nums:
            # original Moore's voting algorithm
            if not count:
                candidate, count = num, 1
            elif candidate == num:
                count += 1
            else:
                count -= 1
        return candidate if nums.count(candidate) > len(nums)//2 else None

# test
print(Solution().majorityElement([1,1,1,1,2,3,4]))
print(Solution().majorityElement2([1,1,1,1,2,3,4]))
print(Solution().majorityElement3([1,1,1,1,2,3,4]))
print(Solution().majorityElement([1,1,1,2,3,4]))
print(Solution().majorityElement2([1,1,1,2,3,4]))
print(Solution().majorityElement3([1,1,1,2,3,4]))
