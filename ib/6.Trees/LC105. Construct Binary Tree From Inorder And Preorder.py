'''
Given preorder and inorder traversal of a tree, construct the binary tree.

 Note: You may assume that duplicates do not exist in the tree.
Example :

Input :
        Preorder : [1, 2, 3]
        Inorder  : [2, 1, 3]

Return :
            1
           / \
          2   3
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # the first item x in preorder is always the current root
    # all items before x in inorder are left children of x
    # all items after x in inorder are right children of x
    # Destructive - preorder is modified
    # slow because of pop(0), index(), and slicing
    def buildTree(self, preorder, inorder):
        if inorder:
            root = TreeNode(preorder.pop(0))
            inorder_ix = inorder.index(root.val)
            # must set left first and then right because of preorder
            root.left  = self.buildTree(preorder, inorder[:inorder_ix])
            root.right = self.buildTree(preorder, inorder[inorder_ix+1:])
            return root

    # faster! use index instead slicing, dict lookup, and inorder index by ref
    # non-destructive
    def buildTree2(self, preorder, inorder):
        def build(inorder_start, inorder_end):
            if inorder_start < inorder_end:
                root = TreeNode(preorder[self.preorder_ix])
                inorder_ix = inorder_dict[root.val]
                self.preorder_ix += 1
                root.left = build(inorder_start, inorder_ix)
                root.right = build(inorder_ix+1, inorder_end)
                return root
        inorder_dict = {v:i for i, v in enumerate(inorder)}
        self.preorder_ix = 0 # the cur index of preorder - pass by reference
        return build(0, len(inorder)) # NOT len-1!!

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, serialize_tree_to_array
inorder  = [9, 5, 1, 7, 2, 12, 8, 4, 3, 11]
preorder = [8, 5, 9, 7, 1, 12, 2, 4, 11, 3]
'''
     8
   /   \
  5     4
 / \     \
9  7     11
  / \    /
 1  12  3
    /
   2
'''
# test
print(serialize_tree_to_array(Solution().buildTree(preorder[:], inorder)))
print(serialize_tree_to_array(Solution().buildTree2(preorder, inorder)))
