'''
Given an array S of n integers, find three integers in S such that the sum is
closest to a given number, target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
Example:
given array S = {-1 2 1 -4},
and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    # O(N^2)
    # similar to lc015. 3Sum.py
    def threeSumClosest(self, A, B):
        A.sort()
        res = float('inf')
        for i in range(len(A)): # fixing i and check possible j, k
            j = i + 1
            k = len(A) - 1
            while j < k:
                # update closest sum to B
                new_sum = A[i] + A[j] + A[k]
                if abs(new_sum - B) < abs(res - B):
                    res = new_sum
                # move j or k by comparing new_sum with B
                if new_sum > B:
                    k -= 1
                elif new_sum < B:
                    j += 1
                else: # early exist found exact B
                    return new_sum
        return res

# test
print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
