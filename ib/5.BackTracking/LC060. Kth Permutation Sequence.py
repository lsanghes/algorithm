'''
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3 ) :

1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"
Given n and k, return the kth permutation sequence.

For example, given n = 3, k = 4, ans = "231"

 Good questions to ask the interviewer :
What if n is greater than 10. How should multiple digit numbers be represented
in string?
> In this case, just concatenate the number to the answer.
> so if n = 11, k = 1, ans = "1234567891011"
Whats the maximum value of n and k?
> In this case, k will be a positive integer thats less than INT_MAX.
> n is reasonable enough to make sure the answer does not bloat up a lot.
'''
class Solution:
    # P(n,k) = n!/(n-k)! >> P(n,n) = n!
    # eg 1234
    # the 1st 6 permuatation(3!) start with 1
    # the 2nd 6 permuatation(3!) start with 2
    def getPermutation(self, n, k):
        from math import factorial
        nums = list(range(1, n+1))
        res = ''
        k -= 1 # index for kth item
        while len(res) < n:
            next_num, k = divmod(k, factorial(n-1))
            res += str(nums.pop(next_num))
        return res

    # bruteforce list all permutations and take kth item
    def getPermutation2(self, n, k):
        from itertools import permutations
        perms = permutations(map(str, range(1, n+1)), n)
        kth = list(perms)[k-1]
        return ''.join(kth)

# test
print(Solution().getPermutation(4,7))
print(Solution().getPermutation2(4,7))
