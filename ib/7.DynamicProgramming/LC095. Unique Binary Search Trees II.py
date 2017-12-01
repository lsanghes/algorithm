'''
Given an integer n, generate all structurally unique BST's (binary search trees)
that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # DP topdown resursive with memo
    def generateTrees(self, n):
        def generate(start, end):
            if start > end:
                return [None]
            if (start, end) in memo:
                return memo[(start, end)]
            res = []
            for i in range(start, end+1):
                for left in generate(start, i-1):
                    for right in generate(i+1, end):
                        node = TreeNode(i)
                        node.left, node.right = left, right
                        res.append(node)
            memo[(start, end)] = res
            return res
        if not n:
            return []
        memo = {}
        return generate(1, n)

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, serialize_tree_to_array
# test
for root in Solution().generateTrees(3):
    print(serialize_tree_to_array(root))
