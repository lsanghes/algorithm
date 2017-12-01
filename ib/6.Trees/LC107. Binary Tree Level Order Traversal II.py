'''
Given a binary tree, return the bottom-up level order traversal of its nodes'
values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
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
    def levelOrderBottom(self, root):
        res = []
        if root:
            level = [root]
            while level:
                res.append([node.val for node in level])
                level = [leaf for node in level
                                for leaf in (node.left, node.right) if leaf]
        return res[::-1]

    # bfs
    def levelOrderBottom2(self, root):
        from collections import deque
        queue = deque([root])
        res = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return res[::-1]

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, build_tree_from_list
# test
root = build_tree_from_list([3,9,20,None,None,15,7])
print(Solution().levelOrderBottom2(root))
print(Solution().levelOrderBottom2(root))
