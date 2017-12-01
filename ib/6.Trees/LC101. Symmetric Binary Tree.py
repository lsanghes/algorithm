'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric
around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetric(self, root):
        # resursively compare left child and right child
        def isMirror(L, R):
            if L and R and L.val == R.val:
                return isMirror(L.left, R.right) and isMirror(L.right, R.left)
            elif L == R == None:
                return True
            else:
                return False
        return isMirror(root, root)

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, build_tree_from_list
# test
print(Solution().isSymmetric(build_tree_from_list([1,2,2,3,4,4,3])))
print(Solution().isSymmetric(build_tree_from_list([1,2,2,None,3,None,3])))
print(Solution().isSymmetric(build_tree_from_list([1,2,2,None,3,3,None])))
