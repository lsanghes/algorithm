'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in
the list, only nodes itself can be changed.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            a, b = cur.next, cur.next.next
            cur.next, b.next, a.next = b, a, b.next # swap
            cur = cur.next.next # link is restored after swap
        return dummy.next

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from LinkedList import ListNode, generate_linked_list, print_linked_list
# test
node = generate_linked_list([1,2,3,4])
node = Solution().swapPairs(node)
print_linked_list(node)
