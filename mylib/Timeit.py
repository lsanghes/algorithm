# timeit does not take parameter.
class Solution:
    def function1(self, n):
        return n ** 100
    def function2(self, n):
        return n ** 100

inputs = 1000
from timeit import timeit
def helper1(): return Solution().function1(inputs)
def helper2(): return Solution().function2(inputs)
print(timeit(helper1, number = 100000))
print(timeit(helper2, number = 100000))
