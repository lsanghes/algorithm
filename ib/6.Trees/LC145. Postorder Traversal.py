'''
Given a binary tree, return the postorder traversal of its nodes’ values.

Example :

Given binary tree

   1
    \
     2
    /
   3
return [3,2,1].

Using recursion is not allowed.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # resursive
    def postorderTraversal(self, root):
        def helper(root):
            if root:
                helper(root.left)
                helper(root.right)
                res.append(root.val)
        res = []
        helper(root)
        return res

    # generic iterative traversal
    def postorderTraversal2(self, root):
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if not visited: # append in reversed order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                else:
                    res.append(node.val)
        return res

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, build_tree_from_list
# test
root = build_tree_from_list([1,None,2,3,None])
print(Solution().postorderTraversal(root))
print(Solution().postorderTraversal2(root))
