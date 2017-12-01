'''
For Given Number N find if its COLORFUL number or not

Return 0/1

COLORFUL number:

A number can be broken into different contiguous sub-subsequence parts.
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
And this number is a COLORFUL number, since product of every digit of a
contiguous subsequence is different
Example:

N = 23
2 3 23
2 -> 2
3 -> 3
23 -> 6
this number is a COLORFUL number since product of every digit of a sub-sequence
are different.

Output : 1
'''
class Solution:
    # @param A : integer
    # @return an integer
    # use slicing to test all contiguous subarry for dup product
    def colorful(self, A):
        def product(nums):
            p = 1
            for n in nums:
                p *= n
            return p
        nums = [int(i) for i in str(A)]
        products = set()
        while nums:
            for i in range(1, len(nums)+1):
                p = product(nums[:i])
                if p in products:
                    return False
                products.add(p)
            nums = nums[1:]
        return True

# test
print(Solution().colorful(3245))
print(Solution().colorful(123))
print(Solution().colorful(2432))
