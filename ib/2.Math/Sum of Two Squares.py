'''
Given a non negative integer A,
following code tries to find all pair of integers (a, b) such that

a and b are positive integers
a <= b, and
a^2 + b^2 = A.
0 <= A <= 100000
However, the code has a small bug. Correct the bug and submit the code.
'''
class Solution:
    def squareSum(self, A):
        res = []
        a = 1
        while a * a <= A//2:
            b = a
            while a * a + b * b <= A:
                if a * a + b * b == A:
                    res.append([a, b])
                    break
                b += 1
            a += 1
        return res

# test
for n in range(0, 100000, 10001):
    pairs = Solution().squareSum(n)
    print('{} : {}'.format(n, pairs))
