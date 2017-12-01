'''
Merge k sorted linked lists and return it as one sorted list. Analyze and
describe its complexity.

Subscribe to see which companies asked this question
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # python native sort
    # since lists are already sorted, python's tim sort use only O(N)
    # so this bruteforce is very efficient!
    def mergeKLists(self, lists):
        items = []
        for node in lists:
            while node:
                items.append(node.val)
                node = node.next
        dummy = cur = ListNode(None)
        for i in sorted(items):
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next

    # using heaps - pyhton heapq is minimun heap
    # O(nlogk) where n = total elements, k = number of lists
    # heappush and heappop takes logK time, and maintain heap invariant
    # we only maintain heap size equal to k, not n !
    def mergeKLists2(self, lists):
        from heapq import heappush, heappop
        heap = []
        for node in lists:
            if node: # check empty list
                heappush(heap, (node.val, node)) # min heap based on node.val
        dummy = cur = ListNode(None)
        while heap:
            val, node = heappop(heap) # pop the min item
            cur.next = node
            cur = cur.next
            if node.next:
                heappush(heap, (node.next.val, node.next))
        return dummy.next

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from LinkedList import ListNode, generate_linked_list, print_linked_list
# test
a = generate_linked_list([2,3,5])
b = generate_linked_list([1,4,6])
print_linked_list(Solution().mergeKLists([a, b]))
print_linked_list(Solution().mergeKLists2([a, b]))
