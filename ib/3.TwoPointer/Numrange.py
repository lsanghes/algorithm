'''
Given an array of non negative integers A, and a range (B, C),
find the number of continuous subsequences in the array which have sum S in the
range [B, C] or B <= S <= C

Continuous subsequence is defined as all the numbers A[i], A[i + 1], .... A[j]
where 0 <= i <= j < size(A)

Example :

A : [10, 5, 1, 0, 2]
(B, C) : (6, 8)
ans = 3
as [5, 1], [5, 1, 0], [5, 1, 0, 2] are the only 3 continuous subsequence with
their sum in the range [6, 8]

NOTE : The answer is guranteed to fit in a 32 bit signed integer.
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer

    # O(N^2) - two pointer test all combination
    def numRange(self, A, B, C):
        count = 0
        for j in range(len(A)):
            k = j
            cur_sum = 0
            while k < len(A):
                cur_sum += A[k]
                if B <= cur_sum <= C:
                    count += 1
                if cur_sum > C: # assume non-negative array
                    break
                k += 1
        return count

    # 6   0   1   5   4   3    count
    # ji  k                    1
    # j   ki                   1
    # j   k   i                1
    #     j       i   k        3
    #     j           ki       3
    #                 j   ki   1
    # O(N) - i, j, k loop at most n times
    # maintain rolling windows
    # shortest possible range is [k-1, i] for each i
    # longest possible range is [j, i] for each i
    def numRange2(self, A, lo, hi):
        j = k = sum_j = sum_k = res = 0
        for i in range(len(A)): # i is the END index
            sum_j += A[i]
            sum_k += A[i]
            while sum_k >= lo and k <= i:
                sum_k -= A[k]
                k += 1
            # now k-1 is the max START index, sum < lo if k move to the right
            while sum_j > hi and j <= k:
                sum_j -= A[j]
                j += 1
            # now j is the min START index, sum > hi if j move to the left
            # subarrays START at j,j+1, ... k-1, and END at i are in range
            res += k - j
        return res

    # if we need to generate all ranges
    # O(max(n,t)), where t is the size of the output.
    # the output can be as large as t = n^2
    def numRange3(self, A, lo, hi):
        j = k = sum_j = sum_k = 0
        res = []
        for i in range(len(A)): # i is the ending point
            sum_j += A[i]
            sum_k += A[i]
            while sum_k >= lo and k <= i:
                sum_k -= A[k]
                k += 1
            # now k-1 is the max START index, sum < lo if k move to the right
            while sum_j > hi and j <= k:
                sum_j -= A[j]
                j += 1
            # now j is the min START index, sum > hi if j move to the left
            # subarrays START at j,j+1, ... k-1, and END at i are in range
            for x in range(j, k):
                res.append(A[x:i+1])
        return res

# test
print(Solution().numRange ([6,0,1,5,4,3], 5, 10))
print(Solution().numRange2([6,0,1,5,4,3], 5, 10))
print(Solution().numRange3([6,0,1,5,4,3], 5, 10))
print(Solution().numRange ([6,0,1,5,4,3], 0, 5))
print(Solution().numRange2([6,0,1,5,4,3], 0, 5))
print(Solution().numRange3([6,0,1,5,4,3], 0, 5))
print(Solution().numRange([1], 0, 0))
print(Solution().numRange2([1], 0, 0))
print(Solution().numRange3([1], 0, 0))
