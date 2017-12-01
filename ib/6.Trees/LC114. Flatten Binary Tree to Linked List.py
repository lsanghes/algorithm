'''
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    # resursive & inplace
    # point the tail of left (inorder predecesoor) to the head of right.
    def flatten(self, root):
        cur = root
        if cur:
            if cur.left:
                # find the inorder predecesoor of curent node
                pre = cur.left
                while pre.right:
                    pre = pre.right
                # pre is now the inorder predecesoor
                pre.right = cur.right
                cur.left, cur.right = None, cur.left
            self.flatten(cur.right) # cur.left is always empty

    # iterative & inplace - same idea but traverse to the right
    def flatten2(self, root):
        cur = root
        while cur:
            if cur.left:
                # find the inorder predecesoor of curent node
                pre = cur.left
                while pre.right:
                    pre = pre.right
                # pre is the inorder predecesoor
                pre.right = cur.right
                cur.left, cur.right = None, cur.left
            cur = cur.right # cur.left is always empty

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, build_tree_from_list, serialize_tree_to_array
# test
root = build_tree_from_list([1,2,5,3,4,None,6])
Solution().flatten(root)
print(serialize_tree_to_array(root))
root = build_tree_from_list([1,2,5,3,4,None,6])
Solution().flatten2(root)
print(serialize_tree_to_array(root))
