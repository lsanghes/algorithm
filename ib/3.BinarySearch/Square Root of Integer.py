'''
Implement int sqrt(int x).

Compute and return the square root of x.

If x is not a perfect square, return floor(sqrt(x))

Example :

Input : 11
Output : 3
DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY
'''
class Solution:
    # @param A : integer
    # @return an integer
    # binary search for n such at a^2 <= A and (a+1)^2 > A
    def sqrt(self, A):
        lo, hi = 0, A
        while lo <= hi:
            mid = (lo + hi)//2
            if mid**2 > A:
                hi = mid - 1
            elif (mid + 1)**2 <= A:
                lo = mid + 1
            else: # mid^2 <= A and (mid+1)^2 > A
                return mid

# test
for i in range(1, 50, 6):
    print((i, Solution().sqrt(i)))
