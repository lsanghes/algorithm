'''
Given a binary search tree, write a function to find the kth smallest element
in the tree.

Example :

Input :
  2
 / \
1   3

and k = 2

Return : 2

As 2 is the second smallest element in the tree.
 NOTE : You may assume 1 <= k <= Total number of nodes in BST
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # use in order generator
    def kthSmallest(self, root, k):
        def in_order(root):
            if not root: return
            for val in in_order(root.left): yield val
            yield root.val
            for val in in_order(root.right): yield val
        res = None
        for val in in_order(root):
            if not k:
                break
            res, k = val, k-1
        return res

    # same idea without using generator
    def kthSmallest2(self, root, k):
        def helper(root):
            if root and self.k:
                helper(root.left)
                self.res = root.val
                self.k -= 1
                helper(root.right)
        self.res = None # use self to pass primative by reference
        self.k = k      # use self to pass primative by reference
        helper(root)
        return self.res

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, build_tree_from_list
# test
root = build_tree_from_list([2,1,3])
print(Solution().kthSmallest(root, 2))
print(Solution().kthSmallest2(root, 2))
