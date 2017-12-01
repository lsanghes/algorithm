'''
               root
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
'''
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.prefix_num = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for letter in word:
            current = current.children.setdefault(letter, TrieNode())
            current.prefix_num += 1
        current.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True

    def prefix_num(self, prefix):
        """
        Returns the number of words in the trie
        that starts with the give nprefix
        :type prefix: str
        :rtype: int
        """
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return 0
            current = current.children[letter]
        return current.prefix_num

# test
trie = Trie()
for w in ['zebra', 'dog', 'duck', 'dot']:
    trie.insert(w)
print(trie.startsWith("z"))
print(trie.search("dog"))
print(trie.search("do"))
print(trie.prefix_num("z"))
print(trie.prefix_num("do"))
