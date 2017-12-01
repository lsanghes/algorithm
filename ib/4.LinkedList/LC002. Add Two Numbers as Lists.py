'''
You are given two linked lists representing two non-negative numbers. The
digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Subscribe to see which companies asked this question
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list

    # whenever A or B or carry is not empty, create a new node
    def addTwoNumbers(self, A, B):
        dummy = node = ListNode(None)
        carry = 0
        while A or B or carry:
            a_val = A.val if A else 0
            b_val = B.val if B else 0
            total = a_val + b_val + carry
            carry, cur_val = divmod(total, 10)
            node.next = ListNode(cur_val)
            node = node.next
            if A:
                A = A.next
            if B:
                B = B.next
        return dummy.next

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from LinkedList import ListNode, generate_linked_list, print_linked_list
# test
a = generate_linked_list([2,4,3])
b = generate_linked_list([5,6,4])
node = Solution().addTwoNumbers(a, b)
print_linked_list(node)
