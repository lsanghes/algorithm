'''
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
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
    def levelOrder(self, root):
        res = []
        if root:
            level = [root]
            while level:
                res.append([node.val for node in level])
                level = [leaf for node in level
                                for leaf in (node.left, node.right) if leaf]
        return res

    # bfs
    def levelOrder2(self, root):
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
        return res

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, build_tree_from_list
# test
root = build_tree_from_list([3,9,20,None,None,15,7])
print(Solution().levelOrder(root))
print(Solution().levelOrder2(root))
