'''
Given inorder and postorder traversal of a tree, construct the binary tree.

 Note: You may assume that duplicates do not exist in the tree.
Example :

Input :
        Inorder : [2, 1, 3]
        Postorder : [2, 3, 1]

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
    # the last item x in postorder is always the current root
    # all items before x in inorder are left children of x
    # all items after x in inorder are right children of x
    # Destructive - postorder is modified
    # slow because of pop(0), index(), and slicing
    def buildTree(self, inorder, postorder):
        if inorder:
            root = TreeNode(postorder.pop())
            inorder_ix = inorder.index(root.val)
            # must set right first and then left because of postorder
            root.right = self.buildTree(inorder[inorder_ix+1:], postorder)
            root.left  = self.buildTree(inorder[:inorder_ix],   postorder)
            return root

    # faster! use index instead slicing, dict lookup, and inorder index by ref
    # non-destructive
    def buildTree2(self, inorder, postorder):
        def build(inorder_start, inorder_end):
            if inorder_start < inorder_end:
                root = TreeNode(postorder[self.postorder_ix])
                inorder_ix = inorder_dict[root.val]
                self.postorder_ix -= 1
                root.right = build(inorder_ix+1, inorder_end)
                root.left = build(inorder_start, inorder_ix)
                return root
        inorder_dict = {v:i for i, v in enumerate(inorder)}
        # the cur index of postorder - pass by reference
        self.postorder_ix = len(postorder)-1
        return build(0, len(inorder)) # NOT len-1!!

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, serialize_tree_to_array
inorder  = [9, 5, 1, 7, 2, 12, 8, 4, 3, 11]
postorder= [9, 1, 2, 12, 7, 5, 3, 11, 4, 8]
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
print(serialize_tree_to_array(Solution().buildTree(inorder, postorder[:])))
print(serialize_tree_to_array(Solution().buildTree2(inorder, postorder)))
