class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

def generate_linked_list(array):
    dummy = cur = ListNode(None)
    for a in array:
        cur.next = ListNode(a)
        cur = cur.next
    return dummy.next

def linked_list_to_array(head):
    if detect_linked_list_cycle(head):
        raise Exception('deteced loop in linked list!')
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def print_linked_list(head):
    if detect_linked_list_cycle(head):
        raise Exception('deteced loop in linked list!')
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(' -> '.join(res))

def reverse_linked_list(head):
    # inplace but input is modified
    rev = None
    while head:
        rev, rev.next, head = head, rev, head.next
    return rev

def reverse_linked_list2(head):
    # non-destructive but need extra space O(N))
    rev = None
    while head:
        rev = ListNode(head.val, rev)
        head = head.next
    return rev

def detect_linked_list_cycle(head):
    try:
        slow, fast = head, head.next
        while slow != fast :
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False

# test
# head = generate_linked_list(list(range(10)))
# print_linked_list(head)
# print_linked_list(reverse_linked_list(head)) # destructive reverse
# print_linked_list(head)
# head = generate_linked_list(list(range(10)))
# print_linked_list(head)
# print_linked_list(reverse_linked_list2(head)) # non-destructive reverse
# print_linked_list(head)
