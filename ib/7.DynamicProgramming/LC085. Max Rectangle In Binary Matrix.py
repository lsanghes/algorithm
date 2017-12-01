'''
Given a 2D binary matrix filled with 0’s and 1’s, find the largest rectangle
containing all ones and return its area.

Bonus if you can solve it in O(n^2) or less.

Example :

A : [  1 1 1
       0 1 1
       1 0 0
    ]

Output : 4

As the max area rectangle is created by the 2x2 rectangle created by (0,1),
(0,2), (1,1) and (1,2)
'''
class Solution:
    # dp solution O(m*n)
    # process row by row from the top, find the max left, min right and height
    # https://discuss.leetcode.com/topic/6650/share-my-dp-solution
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        n = len(matrix[0])
        left, right, height = [0] * n, [n-1] * n, [0] * n
        max_area = 0
        for row in matrix:
            # calculate height - height reset to 0 if cell val is 0
            for c in range(n):
                height[c] = height[c] + 1 if row[c] == '1' else 0
            # calculate left
            cur_left = 0
            for c in range(n):
                # when row[c] is 0, left[c] can be set to any val <= 0 because
                # its height is 0. but it must be small enough so that next
                # row's left val can be set correctly
                left[c] = max(left[c], cur_left) if row[c] == '1' else 0
                if row[c] == '0':
                    cur_left = c + 1
            # calculate right
            cur_right = n - 1
            for c in reversed(range(n)):
                # when row[c] is 0, right[c] can be set to any val >= n-1
                # because its height is 0. but it must be big enough so that
                # next row's right val can be set correctly
                right[c] = min(right[c], cur_right) if row[c] == '1' else n-1
                if row[c] == '0':
                    cur_right = c - 1
            # calculate max_area
            for c in range(n):
                max_area = max(max_area, (right[c] - left[c] + 1) * height[c])
        return max_area

    # using largest rectangle in histogram lc084 - O(m*n)
    # for each row calculate the heights array and treat it as historgram
    def maximalRectangle2(self, matrix):
        if not matrix:
            return 0
        heights = [0] * len(matrix[0])
        max_area = 0
        for row in matrix:
            # calculate the height for each row
            for c in range(len(row)):
                heights[c] = heights[c] + 1 if row[c] == '1' else 0
            # treat heights as histogram
            heights.append(0)
            stack = [-1] # previous index with smaller height
            for i, height in enumerate(heights):
                while height < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - 1 - stack[-1]
                    max_area = max(max_area, h * w)
                stack.append(i)
            heights.pop()
        return max_area

# test
print(Solution().maximalRectangle(["1"]))
print(Solution().maximalRectangle(["10"]))
print(Solution().maximalRectangle(["01","10"]))
print(Solution().maximalRectangle(["10100","10111","11111","10010"]))
print(Solution().maximalRectangle2(["1"]))
print(Solution().maximalRectangle2(["10"]))
print(Solution().maximalRectangle2(["01","10"]))
print(Solution().maximalRectangle2(["10100","10111","11111","10010"]))
