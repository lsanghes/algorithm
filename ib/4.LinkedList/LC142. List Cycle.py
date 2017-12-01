'''
Given a linked list, return the node where the cycle begins. If there is no
cycle, return null.

Try solving it using constant additional space.

Example :

Input :

                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4

Return the node corresponding to node 3.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # slow takes k steps to meet, fast takes 2k steps to meet
    # r = steps within entire cycle/circle
    # 2k-k = n*r  >>  k = n*r
    # s = starting point to cycle entry
    # m = steps from cycle entry to meeting point
    # k = s+m >> s = n*r-m >> s = (n-1)*r+(r-m)
    # i.e. steps from start to cycle entry = steps from meet to cycle entry(r-m)
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hasCycle = False # same as lc141
        start = slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                hasCycle = True
                break
        if hasCycle:
            # slow and start with meet at cycle entry again
            while start != slow:
                start, slow = start.next, slow.next
            return start
        else:
            return None

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from LinkedList import ListNode, generate_linked_list, print_linked_list
# test
node = generate_linked_list([1,2,3,4])
print(Solution().detectCycle(node))
# link node 4 to node 3
node.next.next.next.next = node.next.next
print(Solution().detectCycle(node).val)
# link node 1 to itself
node.next = node
print(Solution().detectCycle(node).val)
