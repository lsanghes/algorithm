'''Given an array, find the next greater element G[i] for every element A[i] in
the array. The Next greater Element for an element A[i] is the first greater
element on the right side of A[i] in array.
More formally,

G[i] for an element A[i] = an element A[j] such that
    j is minimum possible AND
    j > i AND
    A[j] > A[i]
Elements for which no greater element exist, consider next greater element as
-1.

Example:

Input : A : [4, 5, 2, 10]
Output : [5, 10, 10, -1]

Example 2:

Input : A : [3, 2, 1]
Output : [-1, -1, -1]
'''

class Solution:
    # @param A : list of integers
    # @return a list of integers

    # same idea as Nearest Smaller Element.py but reversed order
    def nextGreater(self, A):
        from collections import deque
        stack = deque()
        res = deque()
        for a in reversed(A):
            while stack and stack[0] <= a:
                stack.popleft()
            if stack:
                res.appendleft(stack[0])
            else:
                res.appendleft(-1)
            stack.appendleft(a)
        return list(res)

# test
print(Solution().nextGreater([4, 5, 2, 10]))
print(Solution().nextGreater([3, 2, 1]))
