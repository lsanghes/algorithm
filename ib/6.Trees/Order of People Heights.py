'''You are given the following :

A positive number N
Heights : A list of heights of N persons standing in a queue
Infronts : A list of numbers corresponding to each person (P) that gives the
number of persons who are taller than P and standing in front of P
You need to return list of actual order of persons’s height

Consider that heights will be unique

Example

Input :
Heights: 5 3 2 6 1 4
InFronts: 0 1 2 0 3 2
Output :
actual order is: 5 3 2 1 6 4
So, you can see that for the person with height 5, there is no one taller than
him who is in front of him, and hence Infronts has 0 for him.

For person with height 3, there is 1 person ( Height : 5 ) in front of him who
is taller than him.

You can do similar inference for other people in the list.
'''
class Solution:
    # O(n^2) - sort and then find the (N+1)th empty position
    # since we are looping through height in ascending order, cur height is
    # always taller than previous ones.
    # therefore (N+1)th empty position is the correct index for cur height h
    # because all heights taking these empty positions are taller than h
    def order(self, heights, infronts):
        def nth_empty_pos(arr, n):
            for i, a in enumerate(arr):
                if not a: # found a emtpy position
                    n -= 1
                if not n: # Nth empty position
                    return i
        res = [None] * len(heights)
        for h, i in sorted(zip(heights, infronts)):
            # (i+1)th empty position has i empty positions infront
            res[nth_empty_pos(res, i+1)] = h
        return res

    # https://discuss.leetcode.com/topic/24320/line-reconstruction-by-height/9
    # sort people by height desc and then by in_front asc, still O(n^2) due to
    # array insertion. if we loop through heights in desc order, then in_front
    # is the correct position, because all heighs insert after will be smaller
    # than cur height h, and will not change how many taller height infront of
    # h regardless where they will be inserted
    def order2(self, height, in_front):
        res = []
        for h, i in sorted(zip(height, in_front), reverse=True):
            res.insert(i, h)
        return res

    '''
    Advanced Topic: Rope - need a more efficient way for insertion!
    http://qa.geeksforgeeks.org/3974/determine-the-actual-order-heights-google
    https://discuss.leetcode.com/topic/24320/line-reconstruction-by-height/9
    https://en.wikipedia.org/wiki/Rope_%28data_structure%29
    If the binary tree is balanced, time complexity will be O(nlog(n))，worst
    case will be O(n^2) for linear tree.

        _____6(5) ____        |        ______92(5)______
       /              \       |       /                 \
    5(1)               4(1)   |     62(2)               90(1)
     \                        |     /    \                \
      3(1)                    |   49(1)  27(2)            86(2)
       \                      |          /                /
        2(1)                  |        21(1)            59(1)
         \                    |
          1(1)                |
    '''
    def order3(self, height, in_front):
        class Node(object):
            def __init__(self, height):
                self.height = height
                self.left = None
                self.right = None
                self.infront = 1 # total number of left nodes including self

        # the initial weight of each person is the count, compare to each node
        # in the tree, if the weight is less than the node's weight, node's
        # weight + 1, insert the person to the node's left; If the weight is
        # larger than or equal to the node's weight, decrease the person's
        # weight by node's weight, then insert to node's right.
        def insert(root, height, infront):
            if infront < root.infront:
                root.infront += 1
                if not root.left:
                    root.left = Node(height)
                else:
                    insert(root.left, height, infront)
            else:
                if not root.right:
                    root.right = Node(height)
                else:
                    insert(root.right, height, infront - root.infront)

        # in order generator
        def in_order(root):
            if not root: return
            for node in in_order(root.left): yield node
            yield root
            for node in in_order(root.right): yield node

        people = sorted(list(zip(height, in_front)), reverse=True)
        root = Node(people[0][0])
        for i in range(1, len(people)):
            height, infront = people[i]
            insert(root, height, infront)
        return [node.height for node in in_order(root)]


# test
print(Solution().order([5,3,2,6,1,4], [0,1,2,0,3,2]))
print(Solution().order2([5,3,2,6,1,4], [0,1,2,0,3,2]))
print(Solution().order3([5,3,2,6,1,4], [0,1,2,0,3,2]))
# [5, 3, 2, 1, 6, 4]

print(Solution().order([86,92,49,21,62,27,90,59],[2,0,0,2,0,2,1,3]))
print(Solution().order2([86,92,49,21,62,27,90,59],[2,0,0,2,0,2,1,3]))
print(Solution().order3([86,92,49,21,62,27,90,59], [2,0,0,2,0,2,1,3]))
# [49, 62, 21, 27, 92, 90, 59, 86]
