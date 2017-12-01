'''
Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that g is a
divisor of both m and n.
Both m and n fit in a 32 bit signed integer.

Example

m : 6
n : 9

GCD(m, n) : 3
'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer

    # Euclid's algorithm https://en.wikipedia.org/wiki/Greatest_common_divisor
    # gcd(a, 0) = a
    # gcd(a, b) = gcd(b, a % b)
    def gcd(self, A, B):
        return self.gcd(B, A % B) if B else A

    # find all factors for A and B separately, and the gcd of two sets
    def gcd2(self, A, B):
        def allFactors(A):
            factors = set()
            for n in range(1, int(A**0.5)+1):
                if A % n == 0:
                    factors.add(n)
                    factors.add(A//n)
            return factors
        if not A or not B:
            return max(A, B)
        return max(allFactors(A) & allFactors(B))

# test
print(Solution().gcd(6,9))
print(Solution().gcd(5,0))
print(Solution().gcd2(6,9))
print(Solution().gcd2(5,0))
