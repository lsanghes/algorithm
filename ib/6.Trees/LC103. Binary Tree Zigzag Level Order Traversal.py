'''
Given a binary tree, return the zigzag level order traversal of its nodes'
values. (ie, from left to right, then right to left for the next level and
alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # list comprehension
    # same as order level traversal but reverse the list for odd levels
    def zigzagLevelOrder(self, root):
        res = []
        if root:
            level = [root]
            while level:
                level_vals = [node.val for node in level]
                if len(res) % 2 != 0:
                    level_vals = level_vals[::-1]
                res.append(level_vals)
                level = [leaf for node in level
                                for leaf in (node.left, node.right) if leaf]
        return res

    # BFS search
    def zigzagLevelOrder2(self, root):
        from collections import deque
        queue, res = deque([root]), []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if len(res) % 2 != 0:
                level = level[::-1]
            if level:
                res.append(level)
        return res

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, build_tree_from_list
# test
print(Solution().zigzagLevelOrder(build_tree_from_list([3,9,20,None,None,15,7])))
print(Solution().zigzagLevelOrder2(build_tree_from_list([3,9,20,None,None,15,7])))
print(Solution().zigzagLevelOrder(build_tree_from_list([])))
print(Solution().zigzagLevelOrder2(build_tree_from_list([])))
