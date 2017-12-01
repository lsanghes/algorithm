'''
Given an array where elements are sorted in ascending order, convert it to a
height balanced BST.

Balanced tree : a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.
Example :


Given A : [1, 2, 3]
A height balanced BST  :

      2
    /   \
   1     3
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, serialize_tree_to_array
# test
print(serialize_tree_to_array(Solution().sortedArrayToBST([1,2,3])))
print(serialize_tree_to_array(Solution().sortedArrayToBST([1,2,3,4,5,6,7])))
