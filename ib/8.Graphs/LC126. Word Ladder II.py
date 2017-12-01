'''
Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
'''
class Solution:
    # build a backward directed graph, and then dfs all paths
    def findLadders(self, beginWord, endWord, wordList):
        from collections import defaultdict
        def mask_one_char(word):
            return [word[:i] + char + word[i+1:] for i in range(len(word))
                        for char in 'abcdefghijklmnopqrstuvwxyz'
                            if word[i] != char]

        wordList = set(wordList)
        graph = defaultdict(set) # initialize the graph
        graph[beginWord] = set() # initialize the graph
        level = graph # intialize current level
        while level and endWord not in graph:
            next_level = defaultdict(set)
            for word in level:
                for new_word in mask_one_char(word):
                    if new_word in wordList and new_word not in graph:
                        next_level[new_word].add(word)
            level = next_level
            # dict.update() updates graph with the k/v pairs from next_level
            # update() overwrites existing keys but here is only merging
            graph.update(next_level)

        # graph conatins directed graph with endWord as root. use dfs to find
        # all possible paths in the graph. reverse path before adding to res
        res = []
        def dfs_paths(graph, start, goal, path):
            if start == goal:
                res.append(path[::-1]) # reverse of path before adding
            for word in graph[start]:
                # no need to exclude set(path) - no revisit in this graph
                dfs_paths(graph, word, goal, path+[word])
        dfs_paths(graph, endWord, beginWord, [endWord]) # begin with endWord
        return res

    # build a directed graph using level order, and then search all paths
    def findLadders2(self, beginWord, endWord, wordList):
        from collections import defaultdict
        def mask_one_char(word):
            return [word[:i] + char + word[i+1:] for i in range(len(word))
                        for char in 'abcdefghijklmnopqrstuvwxyz'
                            if word[i] != char]
        wordList = set(wordList)

        # build a graph with level order, stop when reaching endWord
        graph = defaultdict(set) # initialize the graph
        level = set([beginWord])
        while level and endWord not in graph:
            next_level = set()
            for word in level:
                for new_word in mask_one_char(word):
                    # new_wrod in current level is not in graph yet!
                    if new_word in wordList and new_word not in graph and new_word not in level:
                        graph[word].add(new_word)
                        next_level.add(new_word)
            level = next_level

        # dfs/bfs all path... bfs result in lexicological order
        queue = [(beginWord, [beginWord])]
        res = []
        while queue:
            vertex, path = queue.pop(0)
            if vertex == endWord:
                res.append(path)
            for v in graph[vertex] - set(path):
                queue.append((v, path + [v]))
        return res

# test
'''
      hit
       |
      hot
    /     \
  lot     dot
   |       |
  log     dog
     \   /
      cog
'''
print(Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log", "cog"]))
print(Solution().findLadders2("hit", "cog", ["hot","dot","dog","lot","log", "cog"]))
print(Solution().findLadders("hot", "dog", ["hot","dog","dot"]))
print(Solution().findLadders2("hot", "dog", ["hot","dog","dot"]))
print(Solution().findLadders("a", "c", ["a","b","c"]))
print(Solution().findLadders2("a", "c", ["a","b","c"]))
print(Solution().findLadders("hot", "cog", ["hot","dot","cog"]))
print(Solution().findLadders2("hot", "cog", ["hot","dot","cog"]))
print(Solution().findLadders("bb", "ab", ["ab"]))
print(Solution().findLadders2("bb", "ab", ["ab"]))
print(Solution().findLadders("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]))
print(Solution().findLadders2("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]))
