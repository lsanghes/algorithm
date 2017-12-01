'''
You are given with an array of 1s and 0s. And you are given with an integer M,
which signifies number of flips allowed. Find the position of zeros which when
flipped will produce maximum continuous series of 1s.

For this problem, return the indices of maximum continuous series of 1s in
order.

Example:

Input :
Array = {1 1 0 1 1 0 0 1 1 1 }
M = 1

Output :
[0, 1, 2, 3, 4]

If there are multiple possible solutions, return the sequence which has the
minimum start index.
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers

    # increase end first, when solution find, then increase start
    # the zeros are kept in between start and end, i.e. continous 1
    # SubStringTwoPointerTemplate.py
    def maxone(self, A, B):
        zeros = 0
        max_start, max_end = 0, 0
        start, end = 0, 0
        while end < len(A):
            if A[end] == 0:
                zeros += 1
            while zeros > B: # increase start till valid
                if A[start] == 0:
                    zeros -= 1
                start += 1
            if end - start > max_end - max_start:
                max_start, max_end = start, end
            end += 1 # increase end till invalid
        return list(range(max_start, max_end + 1))

# test
print(Solution().maxone([0,1,1,1], 0))
print(Solution().maxone([1,1,0,1,1,0,0,1,1,1], 1))
print(Solution().maxone([1,1,0,1,1,0,0,1,1,1], 2))
print(Solution().maxone([1,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,0], 4))
print(Solution().maxone([0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,1,1,0,0,0,0,1,0,1,0,1,1,0,0], 0))
