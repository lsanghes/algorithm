'''
     8
   /   \
  5     4
 / \     \
9  7     11
  / \    /
 1  12  3
    /
   2
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# construct binary tree from array
# root = build_tree_from_list([8,5,4,9,7,None,11,None,None,1,12,3,None,None,None,2])
def build_tree_from_list(array):
    from collections import deque
    if not array:
        return None
    root = TreeNode(array[0])
    queue = deque([root])
    new_node = True # False if only left child is done
    cur = None
    for i in range(1, len(array)):
        node = TreeNode(array[i]) if array[i] else None
        if new_node:
            cur = queue.popleft()
            cur.left = node
            new_node = False
        else:
            cur.right = node
            new_node = True
        if array[i]:
            queue.append(node)
    return root

# serialize the binary tree to array
# the reverse of build_tree_from_list()
def serialize_tree_to_array(root):
    from collections import deque
    queue = deque([root])
    res = []
    while [x for x in queue if x]:
        # stop if all remainings items are None
        node = queue.popleft()
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    return res

# construct binary tree from array - each node must have unique value
# root = build_tree_from_dict({8:(5,4),5:(9,7),4:(None,11),7:(1,12),11:(3,None),12:(2,None)}, 8)
def build_tree_from_dict(d, root):
    if not root:
        return None
    elif root not in d:
        return TreeNode(root)
    else:
        node = TreeNode(root)
        node.left  = build_tree_from_dict(d, d[root][0])
        node.right = build_tree_from_dict(d, d[root][1])
        return node

###############################################################################
# PreOrder traversal - parent, left, right
# 8, 5, 9, 7, 1, 12, 2, 4, 11, 3
###############################################################################
# PreOrder resursive traversal
def pre_order_generator1(root):
    def helper(root):
        if root:
            res.append(root)
            helper(root.left)
            helper(root.right)
    res = []
    helper(root)
    return res

# PreOrder recursive generator
def pre_order_generator2(root):
    if not root: return
    yield root
    for node in pre_order_generator2(root.left): yield node
    for node in pre_order_generator2(root.right): yield node

# PreOrder iterative traversal
def pre_order_generator3(root):
    res, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node:
            if not visited: # append in reversed order
                stack.append((node.right, False))
                stack.append((node.left, False))
                stack.append((node, True))
            else:
                res.append(node)
    return res

# PreOrder iterative generator
def pre_order_generator4(root):
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node:
            if not visited: # append in reversed order
                stack.append((node.right, False))
                stack.append((node.left, False))
                stack.append((node, True))
            else:
                yield node

# PreOrder morris traversal
def pre_order_generator5(root):
    res = []
    cur = root
    while cur:
        if not cur.left: # no left child, just move to the right
            res.append(cur)
            cur = cur.right
        else:
            # find the inorder predecesoor of curent node
            pre = cur.left
            while pre.right and pre.right != cur: # avoid looping
                pre = pre.right
            # pre is now the inorder predecesoor of curent node
            if not pre.right: # cur is unvisited
                res.append(cur)
                pre.right = cur # create temp link
                cur = cur.left
            else: # cur is visited since pre.right = cur
                pre.right = None # remove temp link
                cur = cur.right
    return res

# PreOrder morris generator
def pre_order_generator6(root):
    cur = root
    while cur:
        if not cur.left: # no left child, just move to the right
            yield cur
            cur = cur.right
        else:
            # find the inorder predecesoor of curent node
            pre = cur.left
            while pre.right and pre.right != cur: # avoid looping
                pre = pre.right
            # pre is now the inorder predecesoor of curent node
            if not pre.right: # cur is unvisited
                yield cur
                pre.right = cur # create temp link
                cur = cur.left
            else: # cur is visited since pre.right = cur
                pre.right = None # remove temp link
                cur = cur.right

###############################################################################
# InOrder traversal - left, parent, right
# 9, 5, 1, 7, 2, 12, 8, 4, 3, 11
###############################################################################
# InOrder recursive traversal
def in_order_generator1(root):
    def helper(root):
        if root:
            helper(root.left)
            res.append(root)
            helper(root.right)
    res = []
    helper(root)
    return res

# InOrder recursive generator
def in_order_generator2(root):
    if not root: return
    for node in in_order_generator2(root.left): yield node
    yield root
    for node in in_order_generator2(root.right): yield node

# generic iterative traversal
def in_order_generator3(root):
    res, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node:
            if not visited: # append in reversed order
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
            else:
                res.append(node)
    return res

# InOrder iterative generator
def in_order_generator4(root):
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node:
            if not visited: # append in reversed order
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
            else:
                yield node

# InOrder morris traversal
def in_order_generator5(root):
    res = []
    cur = root
    while cur:
        if not cur.left: # no left child, just move to the right
            res.append(cur)
            cur = cur.right
        else:
            # find the inorder predecesoor of curent node
            pre = cur.left
            while pre.right and pre.right != cur: # avoid looping
                pre = pre.right
            # pre is now the inorder predecesoor of curent node
            if not pre.right: # cur is unvisited
                pre.right = cur # create temp link
                cur = cur.left
            else: # cur is visited since pre.right = cur
                res.append(cur)
                pre.right = None # remove temp link
                cur = cur.right
    return res

# InOrder morris generator
def in_order_generator6(root):
    cur = root
    while cur:
        if not cur.left: # no left child, just move to the right
            yield cur
            cur = cur.right
        else:
            # find the inorder predecesoor of curent node
            pre = cur.left
            while pre.right and pre.right != cur: # avoid looping
                pre = pre.right
            # pre is now the inorder predecesoor of curent node
            if not pre.right: # cur is unvisited
                pre.right = cur # create temp link
                cur = cur.left
            else: # cur is visited since pre.right = cur
                yield cur
                pre.right = None # remove temp link
                cur = cur.right

###############################################################################
# PostOrder traversal - left, right, parent
# 9, 1, 2, 12, 7, 5, 3, 11, 4, 8
###############################################################################
# PostOrder recursive traversal
def post_order_generator1(root):
    def helper(root):
        if root:
            helper(root.left)
            helper(root.right)
            res.append(root)
    res = []
    helper(root)
    return res

# PostOrder recursive traversal
def post_order_generator2(root):
    if not root: return
    for node in post_order_generator2(root.left): yield node
    for node in post_order_generator2(root.right): yield node
    yield root

# PostOrder iterative generator
def post_order_generator3(root):
    res, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node:
            if not visited: # append in reversed order
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                res.append(node)
    return res

# PostOrder iterative generator
def post_order_generator4(root):
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node:
            if not visited: # append in reversed order
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            else:
                yield node

###############################################################################
# LevelOrder - by node
# 8, 5, 4, 9, 7, 11, 1, 12, 3, 2
###############################################################################
# LevelOrder by node traversal list comprehension
def level_order_generator5(root):
    res = []
    if root:
        level = [root]
        while level:
            res.extend(level)
            level = [leaf for node in level
                            for leaf in (node.left, node.right) if leaf]
    return res

# LevelOrder by node generator list comprehension
def level_order_generator6(root):
    if root:
        level = [root]
        while level:
            for node in level: yield node # to yield each node
            level = [leaf for node in level
                            for leaf in (node.left, node.right) if leaf]

# LevelOrder by node traversal BFS
def level_order_generator7(root):
    from collections import deque
    queue = deque([root])
    res = []
    while queue:
        node = queue.popleft()
        if node:
            res.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return res

# LevelOrder by node generator BFS
def level_order_generator8(root):
    from collections import deque
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            yield node
            queue.append(node.left)
            queue.append(node.right)

###############################################################################
# LevelOrder - by level
# [8], [5, 4], [9, 7, 11], [1, 12, 3], [2]
###############################################################################
# LevelOrder by level traversal list comprehenson
def level_order_generator1(root):
    res = []
    if root:
        level = [root]
        while level:
            res.append([node.val for node in level])
            level = [leaf for node in level
                            for leaf in (node.left, node.right) if leaf]
    return res

# LevelOrder by level generator list comprehenson
def level_order_generator2(root):
    if root:
        level = [root]
        while level:
            yield [node.val for node in level] # to yield one level
            level = [leaf for node in level
                            for leaf in (node.left, node.right) if leaf]

# LevelOrder by level traversal BFS
def level_order_generator3(root):
    from collections import deque
    queue = deque([root])
    res = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if level:
            res.append(level)
    return res

# LevelOrder by level generator BFS
def level_order_generator4(root):
    from collections import deque
    queue = deque([root])
    while queue:
        level = [] # the level is outside queue
        for _ in range(len(queue)): # only pop the size of cur queue!
            node = queue.popleft()
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if level: yield level

###############################################################################
# test
###############################################################################
# array = [8,5,4,9,7,None,11,None,None,1,12,3,None,None,None,2]
# root = build_tree_from_list(array)
# serialized_array = serialize_tree_to_array(root)
# print('Original Array               : {}'.format(array))
# print('Serialized Tree              : {}'.format(serialized_array))
# print('PreOrder recursive traversal : {}'.format([node.val for node in pre_order_generator1(root)]))
# print('PreOrder recursive generator : {}'.format([node.val for node in pre_order_generator2(root)]))
# print('PreOrder iterative traversal : {}'.format([node.val for node in pre_order_generator3(root)]))
# print('PreOrder iterative generator : {}'.format([node.val for node in pre_order_generator4(root)]))
# print('PreOrder morris traversal    : {}'.format([node.val for node in pre_order_generator5(root)]))
# print('PreOrder morris generator    : {}'.format([node.val for node in pre_order_generator6(root)]))
# print('InOrder recursive traversal  : {}'.format([node.val for node in in_order_generator1(root)]))
# print('InOrder recursive generator  : {}'.format([node.val for node in in_order_generator2(root)]))
# print('InOrder iterative traversal  : {}'.format([node.val for node in in_order_generator3(root)]))
# print('InOrder iterative generator  : {}'.format([node.val for node in in_order_generator4(root)]))
# print('InOrder morris traversal     : {}'.format([node.val for node in in_order_generator5(root)]))
# print('InOrder morris generator     : {}'.format([node.val for node in in_order_generator6(root)]))
# print('PostOrder recursive traversal: {}'.format([node.val for node in post_order_generator1(root)]))
# print('PostOrder recursive generator: {}'.format([node.val for node in post_order_generator2(root)]))
# print('PostOrder iterative traversal: {}'.format([node.val for node in post_order_generator3(root)]))
# print('PostOrder iterative generator: {}'.format([node.val for node in post_order_generator4(root)]))
# print('LevelOrder by node list tra  : {}'.format([node.val for node in level_order_generator5(root)]))
# print('LevelOrder by node list gen  : {}'.format([node.val for node in level_order_generator6(root)]))
# print('LevelOrder by node bfs tra   : {}'.format([node.val for node in level_order_generator7(root)]))
# print('LevelOrder by node bfs gen   : {}'.format([node.val for node in level_order_generator8(root)]))
# print('LevelOrder by level list tra : {}'.format([level for level in level_order_generator1(root)]))
# print('LevelOrder by level list gen : {}'.format([level for level in level_order_generator2(root)]))
# print('LevelOrder by level bfs tra  : {}'.format([level for level in level_order_generator3(root)]))
# print('LevelOrder by level bfs gen  : {}'.format([level for level in level_order_generator4(root)]))
