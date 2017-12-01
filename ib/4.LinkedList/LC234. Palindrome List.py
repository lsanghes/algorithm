'''
Given a singly linked list, determine if its a palindrome.
Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:
- Expected solution is linear in time and constant in space.

For example,12

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param A : head node of linked list
    # @return an integer

    # Destructive !
    # Reverse first half and compare from inner to outer
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast: # odd size linked list
            slow = slow.next
        # At this point rev and slow have the same length
        isPalin = True
        while rev: # cannot use slow, doesn't work if len = 1
            if rev.val != slow.val:
                isPalin = False
                break
            rev, slow = rev.next, slow.next
        return isPalin

    # Non-destructive
    # reversed the first half again while comparing
    def isPalindrome2(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        tail = slow.next if fast else slow
        # At this point rev and tail have the same length
        isPalin = True
        while rev: # cannot use slow, doesn't work if len = 1
            if rev.val != tail.val:
                isPalin = False
            # don't break the loop and reverse the first half again
            # rev must be updated the same time as slow since slow.next
            # changes rev.next
            slow, slow.next, rev = rev, slow, rev.next
            tail = tail.next
        return isPalin

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from LinkedList import ListNode, generate_linked_list, print_linked_list
# test
node = generate_linked_list([1,2,3,2,1])
print(Solution().isPalindrome(node))
print_linked_list(node) # original node is destructed

node = generate_linked_list([1,2,3,2,1])
print(Solution().isPalindrome2(node))
print_linked_list(node) # original node is restored

print(Solution().isPalindrome(generate_linked_list([1,2,3,1])))
print(Solution().isPalindrome2(generate_linked_list([1,2,3,1])))
print(Solution().isPalindrome(generate_linked_list([1])))
print(Solution().isPalindrome2(generate_linked_list([1])))



