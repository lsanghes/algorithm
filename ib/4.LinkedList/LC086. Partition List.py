'''
Given a linked list and a value x, partition it such that all nodes less than x
come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two
partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list

    # put everything smaller than B to the left
    # put everything greater/equl than B to the right
    # join left and right but don't fogrget to terminate right.
    def partition(self, A, B):
        dummy_left = cur_left = ListNode(None)
        dummy_right = cur_right = ListNode(None)
        while A:
            if A.val < B:
                cur_left.next = A
                cur_left = cur_left.next
            else:
                cur_right.next = A
                cur_right = cur_right.next
            A = A.next
        cur_right.next = None # end of right might not be empty!
        cur_left.next = dummy_right.next
        return dummy_left.next

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from LinkedList import ListNode, generate_linked_list, print_linked_list
# test
node = generate_linked_list([1,4,3,2,5,2])
node = Solution().partition(node, 3)
print_linked_list(node)
