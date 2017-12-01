'''
Given n non-negative integers representing the histogram's bar height where the
width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
'''
class Solution:
    # O(n) since each item is pushed and poped from stack exactly once
    def largestRectangleArea(self, heights):
        heights.append(0) # add dummy height to avoid edge case
        stack = [] # previous index with smaller height
        max_area = 0
        for i, height in enumerate(heights):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - 1 - stack[-1] if stack else i
                max_area = max(max_area, w * h)
            stack.append(i)
        heights.pop() # remove dummy height
        return max_area

    # initialize stack with -1 to avoid checking empty stack
    def largestRectangleArea2(self, heights):
        heights.append(0) # add dummy height to avoid edge case
        stack = [-1] # previous index with smaller height
        max_area = 0
        for i, height in enumerate(heights):
            while height < heights[stack[-1]]:
                # stack is never empty since heights are non-negative
                # and heights[stack[0]] is always 0 due to dummy height
                h = heights[stack.pop()]
                w = i - 1 - stack[-1]
                max_area = max(max_area, w * h)
            stack.append(i)
        heights.pop() # remove dummy height
        return max_area

# test
print(Solution().largestRectangleArea([2,1,5,6,2,3]))
print(Solution().largestRectangleArea2([2,1,5,6,2,3]))
