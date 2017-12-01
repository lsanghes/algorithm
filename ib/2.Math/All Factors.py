'''
Given a number N, find all factors of N.

Example:

N = 6
factors = {1, 2, 3, 6}
Make sure the returned array is sorted.
'''
class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        factors = set() # use set to exclude duplicate factors
        upper_limit = int(A**0.5)
        for n in range(1, upper_limit+1):
            if A % n == 0: # n and A/n are factors
                factors.add(n)
                factors.add(A//n)
        return sorted(factors) # convert set to sorted list

# test
for n in range(10, 20):
    factors = Solution().allFactors(n)
    print('{} : {}'.format(n, factors))
