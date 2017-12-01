'''
Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.

 A height balanced BST : a height-balanced binary tree is defined as a binary
 tree in which the depth of the two subtrees of every node never differ by more
 than 1.

Example :

Given A : 1 -> 2 -> 3
A height balanced BST  :

      2
    /   \
   1     3
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # find median and build left & right recursively
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # median_node is the median node (n+1)//2
        median_node, slow.next = slow.next, None
        root = TreeNode(median_node.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(median_node.next)
        return root

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, serialize_tree_to_array
from LinkedList import ListNode, generate_linked_list
# test
print(serialize_tree_to_array(
    Solution().sortedListToBST(generate_linked_list([1,2,3]))))
