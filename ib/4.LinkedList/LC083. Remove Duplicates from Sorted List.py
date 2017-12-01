'''
Given a sorted linked list, delete all duplicates such that each element appear
only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr and curr.next:
            if curr.val != curr.next.val:
                curr = curr.next
            else:
                curr.next = curr.next.next
        return head

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from LinkedList import ListNode, generate_linked_list, print_linked_list
# test
node = generate_linked_list([1,2,3,3,3,4,4,5])
node = Solution().deleteDuplicates(node)
print_linked_list(node)
