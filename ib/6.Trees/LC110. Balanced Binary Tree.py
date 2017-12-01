'''
Given a binary tree, determine if it is height-balanced.

 Height-balanced binary tree : is defined as a binary tree in which the depth
 of the two subtrees of every node never differ by more than 1.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Example :

Input :
          1
         / \
        2   3

Return : True or 1

Input 2 :
         3
        /
       2
      /
     1

Return : False or 0
         Because for the root node, left subtree has depth 2 and right subtree
         has depth 0.
         Difference = 2 > 1.
'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, root):
        def depth(root):
            return 1 + max(depth(root.left), depth(root.right)) if root else 0
        isbal = self.isBalanced
        if not root:
            return True
        depth_diff = abs(depth(root.left) - depth(root.right))
        return depth_diff <=1 and isbal(root.left) and isbal(root.right)

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, build_tree_from_list
# test
print(Solution().isBalanced(build_tree_from_list([1,2,3])))
print(Solution().isBalanced(build_tree_from_list([3,2,None,1])))
