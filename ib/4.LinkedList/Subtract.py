'''
Given a singly linked list, modify the value of first half nodes such that :

1st node’s new value = the last node’s value - first node’s current value
2nd node’s new value = the second last node’s value - 2nd node’s current value,
and so on …

 NOTE :
* If the length L of linked list is odd, then the first half implies at first
floor(L/2) nodes. So, if L = 5, the first half refers to first 2 nodes.
* If the length L of linked list is even, then the first half implies at first
L/2 nodes. So, if L = 4, the first half refers to first 2 nodes.
Example :

Given linked list 1 -> 2 -> 3 -> 4 -> 5,

You should return 4 -> 2 -> 3 -> 4 -> 5
as

for first node, 5 - 1 = 4
for second node, 4 - 2 = 2
Try to solve the problem using constant extra space.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list

    # same idea as lc234.
    # Resever the first half while getting to the middle
    # Reverse the first half again while substract from inner to outer
    def subtract(self, A):
        rev = None
        slow = fast = A
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        tail = slow.next if fast else slow
        # At this point rev and tail have the same length
        while rev: # cannot use slow, doesn't work if len = 1
            rev.val = tail.val - rev.val
            slow, slow.next, rev = rev, slow, rev.next
            tail = tail.next
        return A

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from LinkedList import ListNode, generate_linked_list, print_linked_list
# test
node = generate_linked_list([1,2,3,4,5])
node = Solution().subtract(node)
print_linked_list(node)
