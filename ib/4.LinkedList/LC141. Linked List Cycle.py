'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
        # self.next = None
class Solution:
    # LBYL(loop before you leap) version
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hasCycle = False
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                hasCycle = True
                break
        return hasCycle

    # EAFP(easy to ask for forgiveness than permission) version
    # much faster due to less conditional check
    def hasCycle2(self, head):
        try:
            slow, fast = head, head.next
            while slow != fast :
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from LinkedList import ListNode, generate_linked_list, print_linked_list
# test
node = generate_linked_list([1,2,3,4])
print(Solution().hasCycle(node))
print(Solution().hasCycle2(node))
# link node 4 to node 3
node.next.next.next.next = node.next.next
print(Solution().hasCycle(node))
print(Solution().hasCycle2(node))
# link node 1 to itself
node.next = node
print(Solution().hasCycle(node))
print(Solution().hasCycle2(node))


