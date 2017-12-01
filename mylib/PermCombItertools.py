# https://docs.python.org/3/library/itertools.html
import itertools
'''
product()       p, q, ... [repeat=1]
cartesian product, equivalent to a nested for-loop

permutations()  p[, r]
r-length tuples, all possible orderings, no repeated elements

combinations()  p, r
r-length tuples, in sorted order, no repeated elements

combinations_with_replacement() p, r
r-length tuples, in sorted order, with repeated elements

C(n, k) =  n! / (n-k)!k!
P(n, k) =  n! / (n-k)!
'''
print(list(itertools.product('abc', [1,2,3]))) # cartisan product
input = ['abc', [1,2,3]]
print(list(itertools.product(*input))) # pass a list
print(list(itertools.product([]))) # pass a list
print(list(itertools.permutations([1,2,3], 3))) # P(n, k)
print(list(itertools.combinations([1,2,3], 2))) # C(n, k)
print(list(itertools.combinations_with_replacement([1,2,3], 2)))

from math import factorial
print(factorial(3))
