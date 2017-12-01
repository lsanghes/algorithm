'''
Given a number N, find all prime numbers upto N ( N included ).

Example:

if N = 7,

all primes till 7 = {2, 3, 5, 7}

Make sure the returned array is sorted.
'''
class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        is_prime = [True] * (A+1)
        for i in range(2, int(A**0.5)+1):
            if is_prime[i]:
                for j in range(i+i, A+1, i):
                    # mark multiple of 2s, 3s, 4s ..etc as prime
                    is_prime[j] = False
        return [i for i in range(2, A+1) if is_prime[i]]

# test
prime_nums = Solution().sieve(100)
print(prime_nums)
