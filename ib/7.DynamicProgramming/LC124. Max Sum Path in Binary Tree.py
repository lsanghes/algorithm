'''
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting
node to any node in the tree along the parent-child connections. The path does
not need to go through the root.

For example:
Given the below binary tree,
       1
      / \
     2   3

Return 6.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # pass variable by reference using class variable self.
    # allow -ve node.
    def maxPathSum(self, root):
        # returns the maximum sum of the path that can be extended to input
        # node's parent.
        def get_max_sum(node):
            if not node:
                return 0
            # if path sum of a child is negative, ignore the child.
            left_sum  = max(0, get_max_sum(node.left))
            right_sum = max(0, get_max_sum(node.right))
            # update the max_sum as we traverse through each node
            self.max_sum = max(self.max_sum, left_sum + right_sum + node.val)
            # only return the max of left or right as we cannot traverse both
            return max(left_sum, right_sum) + node.val
        # either use self.max_sum or non-primative type [] to pass by reference
        self.max_sum = float('-inf')
        get_max_sum(root)
        return self.max_sum

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, build_tree_from_list
# test
print(Solution().maxPathSum(build_tree_from_list([1,2,3])))
print(Solution().maxPathSum(build_tree_from_list([1,-2,3])))
