'''
Find the lowest common ancestor in an unordered binary tree given two values
in the tree.

 Lowest common ancestor : the lowest common ancestor (LCA) of two nodes v and w
 in a tree or directed acyclic graph (DAG) is the lowest (i.e. deepest) node
 that has both v and w as descendants.

Example :

         ______3______
        /             \
    ___5__          ___1__
   /      \        /      \
   6      _2_     0        8
         /   \
         7    4
For the above tree, the LCA of nodes 5 and 1 is 3.

 LCA = Lowest common ancestor
Please note that LCA for nodes 5 and 4 is 5.


*******************************************************************************
Additional Requirement from IB: no guarantee that p and q exist, no dup number
*******************************************************************************
You are given 2 values. Find the lowest common ancestor of the two nodes
represented by val1 and val2
No guarantee that val1 and val2 exist in the tree. If one value doesn’t exist
in the tree then return -1.
There are no duplicate values.
You can use extra memory, helper functions, and can modify the node struct but,
you can’t add a parent pointer.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # AC by leetcode. 128 ms
    # handles dup number but not non-exisitance of p or q
    # assume p and q must both exist because:
    # if p is the parent node of q, search stop at p. eg p=5, q=4
    # p and q are treenode instead of val so nodes with dup number may exist
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        left  = self.lowestCommonAncestor(root.left,  p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right

    # AC by both IB and leetcode using iterative dfs but extremely slow! 942 ms
    # handle dup and non-existance of p or q
    # find the path to q and p respectively. e
    # the last common node in path is LCA
    def lowestCommonAncestor2(self, root, p, q):
        stack = [(root, [root])]
        p_path, q_path = [], []
        # find path to p and q if path exist
        while not p_path or not q_path:
            if not stack:
                return -1
            node, path = stack.pop()
            if node == p:
                p_path = path
            if node == q:
                q_path = path
            if node.left:
                stack.append((node.left, path+[node.left]))
            if node.right:
                stack.append((node.right, path+[node.right]))
        # both path found, find last common node in paths
        # lca always exist since root is awlays the common node
        i = 0
        while i < min(len(p_path), len(q_path)):
            if p_path[i] != q_path[i]:
                break
            i+=1
        return p_path[i-1]

    # AC by both IB and leetcode 116ms
    # handle dup and non-existance of p or q
    # similar idea to lowestCommonAncestor2
    # instead of storing entire path, just stored the parent node
    def lowestCommonAncestor3(self, root, p, q):
        stack = [root]
        parent = {root: None} # {cur_node: parent_node}
        while p not in parent or q not in parent:
            if not stack:
                return -1
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        # both node found, find the first common node going backward
        # lca always exist since root is awlays the common node
        p_path = set()
        while p:
            p_path.add(p)
            p = parent[p]
        # find the first node in q's path that's also in p's path
        while q not in p_path:
            q = parent[q]
        return q

    # ib version - same as lowestCommonAncestor3
    # since ib only pass val instead of node, there cannot be dup
    def lca(self, root, pval, qval):
        # @param A : root node of tree
        # @param val1 : integer
        # @param val2 : integer
        # @return an integer
        stack = [root]
        parent = {root.val: None}
        while pval not in parent or qval not in parent:
            if not stack:
                return -1
            node = stack.pop()
            if node.left:
                parent[node.left.val] = node.val
                stack.append(node.left)
            if node.right:
                parent[node.right.val] = node.val
                stack.append(node.right)
        p_path = set()
        while pval:
            p_path.add(pval)
            pval = parent[pval]
        while qval not in p_path:
            qval = parent[qval]
        return qval

# import
import sys, os
sys.path.insert(0, os.path.abspath((os.pardir + os.sep) * 2 + 'mylib'))
from BinaryTreeTraversalGenerator import TreeNode, build_tree_from_list
# test
root = build_tree_from_list([3,5,1,6,2,0,8,None,None,7,4])
p = root.left.left
q = root.left.right.right
print(Solution().lowestCommonAncestor(root, p, q).val)
print(Solution().lowestCommonAncestor2(root, p, q).val)
print(Solution().lowestCommonAncestor2(root, p, q).val)
print(Solution().lca(root, 6, 4))
