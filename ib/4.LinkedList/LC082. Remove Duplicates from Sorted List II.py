'''
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # fast node to check dup, and slow node maintain all num withour dup
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        slow, fast = dummy, dummy.next # no dup up to slow
        while fast and fast.next:
            if fast.val != fast.next.val:
                fast = fast.next
                slow = slow.next
            else:
                while fast.next and fast.val == fast.next.val:
                    fast = fast.next
                slow.next = fast.next # fast is the last dup num
                fast = fast.next
        return dummy.next

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from LinkedList import ListNode, generate_linked_list, print_linked_list
# test
node = generate_linked_list([1,2,3,3,4,4,5])
node = Solution().deleteDuplicates(node)
print_linked_list(node)
