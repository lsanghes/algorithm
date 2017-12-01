'''
Given a binary tree, find its maximum depth.

The maximum depth of a binary tree is the number of nodes along the longest
path from the root node down to the farthest leaf node.

 NOTE : The path has to end on a leaf node.
Example :

         1
        /
       2
max depth = 2.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = self.maxDepth
        return 1 + max(depth(root.left), depth(root.right)) if root else 0

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, build_tree_from_list
# test
print(Solution().maxDepth(build_tree_from_list([1,2,None])))
print(Solution().maxDepth(build_tree_from_list([3,9,20,None,None,15,7])))
