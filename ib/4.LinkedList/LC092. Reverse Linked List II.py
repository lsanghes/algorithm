'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # segment 1 - everything before m
    # segment 2 - reversed m to n
    # segment 3 - everything after m
    # join segement 1, 2, 3
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pre = dummy = ListNode(None)
        dummy.next = head
        for _ in range(m-1): # skip first m element
            pre = pre.next # pre is the end of first segment
        cur = rev_end = pre.next # pre.next will be end of reversed list
        rev = None
        for _ in range(n-m+1): # reversed the list - lc206
            rev, rev.next, cur = cur, rev, cur.next
        pre.next = rev # join segment 1 and 2
        rev_end.next = cur # join segment 2 and 3.
        return dummy.next

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from LinkedList import ListNode, generate_linked_list, print_linked_list
# test
node = generate_linked_list([1,2,3,4,5])
node = Solution().reverseBetween(node, 2, 4)
print_linked_list(node)
