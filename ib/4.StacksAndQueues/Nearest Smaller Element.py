'''
Given an array, find the nearest smaller element G[i] for every element A[i] in
the array such that the element has an index smaller than i.

More formally,

G[i] for an element A[i] = an element A[j] such that
    j is maximum possible AND
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as
-1.

Example:

Input : A : [4, 5, 2, 10]
Return : [-1, 4, -1, 2]

Example 2:

Input : A : [3, 2, 1]
Return : [-1, -1, -1]
'''
class Solution:
    # @param arr : list of integers
    # @return a list of integers
    def prevSmaller(self, arr):
        stack = []
        res = []
        for x in arr:
            while stack and stack[-1] >= x:
                stack.pop()
            if not stack:
                res.append(-1)
            else:
                res.append(stack[-1])
            stack.append(x)
        return res

# test
print(Solution().prevSmaller([4,5,2,10]))
print(Solution().prevSmaller([3,2,1]))
