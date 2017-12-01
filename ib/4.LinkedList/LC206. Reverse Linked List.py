'''
Reverse a linked list. Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL,

# return 5->4->3->2->1->NULL.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, head):
        rev = None
        while head:
            rev, rev.next, head = head, rev, head.next
        return rev

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from LinkedList import ListNode, generate_linked_list, print_linked_list
# test
node = generate_linked_list([1,2,3,4,5])
node = Solution().reverseList(node)
print_linked_list(node)
