'''
Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example :
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from
index 0 to 1, then 3 steps to the last index.)

If it is not possible to reach the end index, return -1.
'''
class Solution:
    # greedy
    # maintain the maximum index that is reachable
    # if we can reach index i then we can at least reach index i+num[i]
    # assume all jumps >= 0
    def jump(self, nums):
        start = end = step = 0
        while end < len(nums) - 1:
            step += 1
            next_max = max([i + nums[i] for i in range(start, end+1)])
            if next_max > end: # we can move forward
                start, end = end + 1, next_max
            else: # cannot move forward
                return -1
        return step

    # bfs - TLE 20
    def jump2(self, nums):
        from collections import deque
        queue = deque([(0,0)])
        visited = set()
        while queue:
            ix, step = queue.popleft()
            if ix == len(nums) - 1:
                return step
            for i in range(nums[ix]):
                new_ix = ix + i + 1
                if new_ix not in visited:
                    queue.append((new_ix, step+1))
                    visited.add(new_ix)
        return -1

# test
nums = [ 23, 18, 19, 17, 41, 0, 22, 0, 15, 48, 5, 0, 25, 29, 33, 16, 35, 0, 45, 46, 37, 46, 13, 0, 9, 0, 47, 26, 0, 46, 33, 0, 40, 20, 42, 18, 7, 0, 20, 0, 31, 17, 34, 0, 0, 18, 0, 6, 16, 7, 23, 0, 13, 46, 49, 33, 43, 15, 18, 29, 40, 42, 50, 2, 37, 0, 13, 0, 49, 4, 34, 47, 34, 48, 0, 0, 0, 49, 22, 0, 1, 35, 47, 33, 3, 19, 23, 39, 0, 14, 9, 0, 4, 7, 26, 0, 6, 31, 0, 13, 44, 0, 1, 49, 5, 40, 50, 4, 0, 13, 38, 35, 0, 0, 48, 0, 35, 26, 0, 47, 38, 35, 0, 0, 0, 16, 0, 33, 9, 29, 39, 38, 44, 25, 0, 0, 50, 13, 0, 44, 11, 1, 0, 45, 0, 11, 37, 0, 28, 23, 4, 7, 0, 0, 29, 44, 0, 29, 0, 0, 25, 40, 0, 0, 47, 12, 4, 35, 46, 40, 5, 47, 35, 3, 27, 0, 44, 22, 48, 45, 32, 30, 0, 13, 0, 0, 4, 9, 0, 20, 43, 37, 0, 39, 46, 29, 33, 21, 50, 0, 19, 36, 0, 6, 45, 21, 0, 40, 0, 0, 50, 4, 0, 32, 0, 28, 0, 44, 18, 30, 32, 0, 12, 10, 0, 0, 8, 43, 0, 37, 48, 0, 14, 11, 23, 27, 29, 44, 21, 1, 0, 0, 0, 30, 24, 0, 21, 10, 41, 35, 49, 25, 0, 43, 39, 15, 48, 0, 19, 28, 40, 0, 16, 30, 43, 6, 19, 5, 32, 35, 15, 26, 47, 0, 37, 40, 41, 49, 0, 0, 20, 11, 0, 46, 0, 29, 0, 22, 0, 0, 0, 25, 0, 43, 32, 0, 0, 42, 0, 10, 31, 32, 3, 0, 45, 49, 33, 50, 13, 16, 40, 46, 19, 35, 20, 16, 5, 32, 0, 0, 29, 16, 14, 0, 44, 23, 0, 2, 15, 15, 12, 48, 50, 20, 7, 0, 30, 32, 45, 0, 40, 0, 1, 44, 0, 13, 0, 21, 47, 0, 0, 9, 0, 3, 44, 28, 50, 0, 48, 27, 4, 31, 6, 43, 0, 2, 0, 15, 41, 20, 0, 0, 5, 22, 0, 48, 25, 30, 21, 27, 14, 5, 7, 45, 21, 20, 0, 13, 0, 13, 0, 14, 36, 36, 21, 0, 29, 30, 0, 18, 18, 12, 0, 0, 17, 39, 44, 21, 14, 0, 26, 45, 11, 11, 43, 35, 30, 5, 0, 30, 1, 0, 34, 0, 13, 21, 0, 0, 45, 48, 32, 41, 5, 0, 0, 1, 34, 50, 30, 25, 12, 26, 0, 43, 0, 34, 21, 0, 23, 48, 0, 0, 0, 0, 0, 45, 43, 5, 11, 34, 0, 42, 9, 44, 38, 0, 3, 42, 50, 0, 0, 26, 50, 17, 27, 23, 13, 3, 17, 4, 8, 3, 32, 47, 36, 13, 10, 0, 9, 43, 19, 32, 0, 43, 40, 0, 16, 0, 0, 24, 43, 28, 49, 33, 49, 23, 8, 48, 42, 18, 35, 1, 13, 18, 5, 27, 10, 35, 3, 45, 2, 1, 7, 40, 40, 0, 0, 44, 6, 0, 29, 0, 8, 34, 28, 0, 23, 20, 24, 1, 2, 47, 20, 5, 16, 0, 37, 25, 0, 0, 26, 7, 0, 46, 40, 3, 34, 6, 2, 0, 22, 0, 46, 1, 37, 29, 3, 1, 0, 0, 0, 0, 6, 19, 0, 0, 38, 23, 18, 38, 26, 28, 40, 49, 9, 47, 26, 0, 0, 2, 0, 0, 43, 0, 3, 18, 1, 48 ]
print(Solution().jump([2,3,1,1,4]))
print(Solution().jump([2,0,0,0,4]))
print(Solution().jump2([2,3,1,1,4]))
print(Solution().jump2([2,0,0,0,4]))
print(Solution().jump(nums))
print(Solution().jump2(nums))

from timeit import timeit
def helper1(): return Solution().jump(nums)
def helper2(): return Solution().jump2(nums)
print(timeit(helper1, number = 100))
print(timeit(helper2, number = 100))
