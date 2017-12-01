'''
You are given an array of N integers, A1, A2 ,…, AN and an integer K. Return
the of count of distinct numbers in all windows of size K.

Formally, return an array of size N-K+1 where i’th element in this array
contains number of distinct elements in sequence Ai, Ai+1 ,…, Ai+k-1.

Note:
- If K > N, return empty array.

For example,

A=[1, 2, 1, 3, 4, 3] and K = 3

All windows of size K are

[1, 2, 1]
[2, 1, 3]
[1, 3, 4]
[3, 4, 3]

So, we return an array [2, 3, 3, 2].
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers

    # bruteforce
    def dNums1(self, A, B):
        res = []
        for i in range(len(A)-B+1):
            res.append(len(set(A[i:i+B])))
        return res

    # sliding window O(N) - window [j,k] contains B elements
    def dNums2(self, A, B):
        from collections import defaultdict
        res = []
        d = defaultdict(int)
        for k, a in enumerate(A):
            d[a] += 1
            if k >= B-1:
                res.append(len(d))
                j = k - B + 1
                char = A[j]
                d[char] -= 1
                if d[char] == 0:
                    del d[char]
        return res

# test
print(Solution().dNums1([1, 2, 1, 3, 4, 3], 3))
print(Solution().dNums2([1, 2, 1, 3, 4, 3], 3))
