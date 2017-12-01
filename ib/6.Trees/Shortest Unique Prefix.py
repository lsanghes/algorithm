'''
Shortest Unique Prefix
Find shortest unique prefix to represent each word in the list.

Example:

Input: [zebra, dog, duck, dot]
Output: {z, dog, du, dot}
where we can see that
zebra = z
dog = dog
duck = du
dot = dot

Now we will build prefix tree and we will also store count of characters
                root(4)
                /|
         (d, 3)/ |(z, 1)
              /  |
          Node1  Node2
           /|        \
     (o,2)/ |(u,1)    \(e,1)
         /  |          \
   Node1.1  Node1.2     Node2.1
      | \         \            \
(g,1) |  \ (t,1)   \(c,1)       \(b,1)
      |   \         \            \
    Leaf Leaf       Node1.2.1     Node2.1.1
    (dog)  (dot)        \                  \
                         \(k, 1)            \(r, 1)
                          \                  \
                          Leaf               Node2.1.1.1
                          (duck)                       \
                                                        \(a,1)
                                                         \
                                                         Leaf
                                                         (zebra)

Now, for every leaf / word , we find the character nearest to the root with
frequency as 1. The prefix that the path from root to this character corresponds
to, is the representation of the word.
'''
class Solution:
    # @param words : list of strings
    # @return words list of strings

    # build implicit prefix tree using dict
    def prefix(self, words):
        tree = [0, {}]
        for word in words:
            node = tree
            for letter in word:
                if letter not in node[1]:
                    node[1][letter] =  [0, {}]
                node = node[1][letter]
                node[0] += 1
        res = []
        for word in words:
            prefix = ''
            node = tree
            for letter in word:
                if node[0] == 1: break
                prefix += letter
                node = node[1][letter]
            res.append(prefix)
        return res

    # Advanced Topic - explicit prefix tree (trie)
    def prefix2(self, words):
        class TrieNode(object):
            def __init__(self):
                self.prefix_num = 0
                self.children = {}
        class Trie(object):
            def __init__(self):
                self.root = TrieNode()
            def insert(self, word):
                current = self.root
                for letter in word:
                    current = current.children.setdefault(letter, TrieNode())
                    current.prefix_num += 1
        trie = Trie()
        for word in words:
            trie.insert(word)
        res = []
        for word in words:
            prefix = ''
            node = trie.root
            for letter in word:
                if node.prefix_num == 1: break
                prefix += letter
                node = node.children[letter]
            res.append(prefix)
        return res

# test
print(Solution().prefix(['zebra', 'dog', 'duck', 'dot']))
print(Solution().prefix2(['zebra', 'dog', 'duck', 'dot']))
