'''
Given an even number ( greater than 2 ), return two prime numbers whose sum will
be equal to given number.

NOTE A solution will always exist. read Goldbach’s conjecture

Example:
Input : 4
Output: 2 + 2 = 4

If there are more than one solutions possible, return the lexicographically
smaller solution.

If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then

[a, b] < [c, d]

If a < c OR a==c AND b < d.
'''
class Solution:
    # @param A : integer
    # @return a list of integers
    # test both x and A-x are prime
    def primesum(self, A):
        def is_prime(n):
            if n < 2: # not needed for this question though.
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        for i in range(2, A):
            if is_prime(i) and is_prime(A-i):
                return [i, A-i]

    # generate all the primes first and choose the first two
    def primesum2(self, A):
        def get_primes_factors(n):
            is_prime = [True] * (n+1)
            for i in range(2, int(n**0.5)+1):
                if is_prime[i]:
                    for j in range(i+i, n+1, i):
                        is_prime[j] = False
            return [i for i in range(2, n+1) if is_prime[i]]
        primes = get_primes_factors(A)
        for p in primes:
            if A - p in primes:
                return [p, A-p]

# test
print(Solution().primesum(10))
print(Solution().primesum2(10))
