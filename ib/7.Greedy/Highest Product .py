'''
Given an array of integers, return the highest product possible by multiplying
3 numbers from the array

Input:

array of integers e.g {1, 2, 3}
 NOTE: Solution will fit in a 32-bit signed integer
Example:

[0, -1, 3, 100, 70, 50]

=> 70*50*100 = 350000
'''
class Solution:
    # O(NlogN) generate -ve and +ve arrays and calculate for each 5 case.
    # a. 3 +ve num
    # b. 2 +ve num and 1 -ve num
    # c. 1 +ve num and 2 -ve num
    # d. 3 -ve num
    # e. contains at least one zero
    def maxp3(self, A):
        A.sort()
        if len(A) < 3:
            return 0
        pos_nums = [a for a in A if a > 0]
        neg_nums = [a for a in A if a < 0]
        a = b = c = d = e = float('-inf')
        if len(pos_nums) >= 3:
            a = pos_nums[-1] * pos_nums[-2] * pos_nums[-3]
        if len(pos_nums) >= 2 and len(neg_nums) >= 1:
            b = pos_nums[-1] * pos_nums[-2] * neg_nums[-1]
        if len(pos_nums) >= 1 and len(neg_nums) >= 2:
            c = pos_nums[-1] * neg_nums[0] * neg_nums[1]
        if len(neg_nums) >= 3:
            d = neg_nums[-1] * neg_nums[-2] * neg_nums[-3]
        if len(neg_nums) + len(neg_nums) < len(A):
            e = 0
        return max(a, b, c, d, e)

    # combine case a,b,d,e
    def maxp3b(self, A):
        A.sort()
        if len(A) < 3:
            return 0
        m1, m2, m3 = A[-1], A[-2], A[-3]
        res = m1 * m2 * m3 # case a, b, d, e
        if A[0] < 0 and A[1] < 0: # case c: at least 2 -ve nums
            res = max(A[0] * A[1] * m1, res)
        return res

# test
print(Solution().maxp3([0,-1,3,100,70,50]))
print(Solution().maxp3([1,3,5,2,8,0,-1,-3]))
print(Solution().maxp3([-1,-2,-3,-4,-5]))
print(Solution().maxp3([1,2,-3]))
print(Solution().maxp3([-2,-1,-3,0]))
print(Solution().maxp3b([0,-1,3,100,70,50]))
print(Solution().maxp3b([1,3,5,2,8,0,-1,-3]))
print(Solution().maxp3b([-1,-2,-3,-4,-5]))
print(Solution().maxp3b([1,2,-3]))
print(Solution().maxp3b([-2,-1,-3,0]))
