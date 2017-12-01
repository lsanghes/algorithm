'''
Implement pow(x, n) % d.

In other words, given x, n and d,

find (x^n % d)

Note that remainders on division cannot be negative.
In other words, make sure the answer you return is non negative.

Input : x = 2, n = 3, d = 3
Output : 2

2^3 % 3 = 8 % 3 = 2.
'''
class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer

    # multiplication property
    # (A * B) mod C = (A mod C * B mod C) mod C
    # addition property
    # (A + B) mod C = (A mod C + B mod C) mod C
    # exponentiation property
    # (A^B) mod C = ((A mod C)^B) mod C
    def pow(self, x, n, d):
        if n <= 1:
            return (x ** n) % d
        a = self.pow(x, n//2, d)
        b = self.pow(x, 1, d)
        if n % 2 == 0:
            return (a * a) % d # multiplication property
        else:
            return (a * a * b) % d # multiplication property

# test
print(Solution().pow(2,3,3))
print(Solution().pow(23,100,3))
