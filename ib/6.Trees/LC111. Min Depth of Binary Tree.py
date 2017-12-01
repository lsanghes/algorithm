'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root
node down to the nearest leaf node.

 NOTE : The path has to end on a leaf node.
Example :

         1
        /
       2
min depth = 2.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        elif not root.left:
            return 1 + self.minDepth(root.right)
        elif not root.right:
            return 1 + self.minDepth(root.left)
        else: # both right and left child exist
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, build_tree_from_list
# test
print(Solution().minDepth(build_tree_from_list([1])))
print(Solution().minDepth(build_tree_from_list([1,2])))
print(Solution().minDepth(build_tree_from_list([1,2,3,4,5])))
print(Solution().minDepth(build_tree_from_list([1,2,3,4,5,6])))
