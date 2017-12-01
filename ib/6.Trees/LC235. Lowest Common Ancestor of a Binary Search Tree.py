'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is
defined between two nodes v and w as the lowest node in T that has both v and w
as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another
example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of
itself according to the LCA definition.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # resursive
    # if p and q are in different sides, then cur node is the LCA
    # otherwise traverse down the tree, either left or right
    # assume p and q always exist
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else: #either p or q is root.val, or p and q on two sides
            return root

    # iterative - same idea.
    # assume p and q always exist
    def lowestCommonAncestor2(self, root, p, q):
        while root:
            if p.val > root.val < q.val:
                root = root.right
            elif p.val < root.val > q.val:
                root = root.left
            else:
                return root

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, build_tree_from_list
# test
root = build_tree_from_list([6,2,8,0,4,7,9,None,None,3,5])
print(Solution().lowestCommonAncestor(root, TreeNode(3), TreeNode(7)).val)
print(Solution().lowestCommonAncestor2(root, TreeNode(3), TreeNode(7)).val)
