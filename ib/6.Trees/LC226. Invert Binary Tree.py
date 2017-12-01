'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you
can’t invert a binary tree on a whiteboard so fuck off.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # inplace - swap left and right child and resursive invert left and right
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

    # inplace - one liner
    def invertTree2(self, root):
        invert = self.invertTree2
        if root:
            root.left, root.right = invert(root.right), invert(root.left)
        return root

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, build_tree_from_list, serialize_tree_to_array
# test
root = build_tree_from_list([4,2,7,1,3,6,9])
print(serialize_tree_to_array(Solution().invertTree(root)))
root = build_tree_from_list([4,2,7,1,3,6,9])
print(serialize_tree_to_array(Solution().invertTree2(root)))
