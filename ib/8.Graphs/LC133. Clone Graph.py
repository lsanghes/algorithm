'''
Clone an undirected graph. Each node in the graph contains a label and a list
of its neighbors.

OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and
each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as
separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a
self-cycle.

Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
'''
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # recursive dfs - memo[node] = clone_node
    def cloneGraph(self, node):
        def clone(node):
            if node not in memo:
                memo[node] = UndirectedGraphNode(node.label)
                memo[node].neighbors = [clone(n) for n in node.neighbors]
            return memo[node]
        if not node:
            return node
        memo = {}
        return clone(node)

    # iterative dfs - memo[node] = clone_node
    def cloneGraph2(self, node):
        if not node:
            return node
        memo = {node:UndirectedGraphNode(node.label)}
        stack = [node]
        while stack:
            cur_node = stack.pop()
            for neighbor in cur_node.neighbors:
                if neighbor in memo:
                    memo[cur_node].neighbors.append(memo[neighbor])
                else:
                    memo[neighbor] = UndirectedGraphNode(neighbor.label)
                    memo[cur_node].neighbors.append(memo[neighbor])
                    stack.append(neighbor)
        return memo[node]

# test
n0,n1,n2 = UndirectedGraphNode(0),UndirectedGraphNode(1),UndirectedGraphNode(2)
n0.neighbors = [n1, n2]
n1.neighbors = [n2]
n2.neighbors = [n2]
n0_clone1 = Solution().cloneGraph(n0)
n0_clone2 = Solution().cloneGraph2(n0)
