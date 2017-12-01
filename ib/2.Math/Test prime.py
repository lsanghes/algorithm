'''
Following code tries to figure out if a number is prime ( Wiki )
However, it has a bug in it.
Please correct the bug and then submit the code.
'''
class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        if A < 2:
            return False
        upperLimit = int(A**0.5) # smaller factor is always smaller than A^0.5
        for i in range(2, upperLimit + 1):
            if A % i == 0: # found a factor
                return False
        return True

# test
for n in range(10, 20):
    is_prime = Solution().isPrime(n)
    print('{} : {}'.format(n, is_prime))
